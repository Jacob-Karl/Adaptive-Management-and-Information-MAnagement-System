import django
import os
import datetime
from django.shortcuts import *
from reports.forms import *
from django.contrib import *
from django.contrib.auth.decorators import login_required
from user_functions.models import *
from projects.models import *
from scopes.models import *
import time

# Create your views here.
@login_required
def hub(request):
    context_dict = {}
    
    all_projects = Project.objects.all()
    context_dict = {
        'All_Projects' : all_projects,
    }
    
    return render(request, 'reports/report_hub.html', context_dict)

@login_required
def prepare_report(request, project_ID):
    report_selector_form = reportSelectorForm(request.POST)
    project = Project.objects.get(pk = project_ID)
    
    context_dict = {
        'project':project,
        'project_ID':project_ID,
        'report_selector_form':report_selector_form,
    }
    
    print(render(request, 'reports/report_hub.html', context_dict))
    if report_selector_form.is_valid():
        return render(request, 'reports/report_hub.html', context_dict)    
    return render(request, 'reports/report.html', context_dict)

#generate report need to be reworked to take the output of the report prepare via the URL
#It then needs to take the input and break when appropriate

@login_required
def generate_project_report(request, project_ID):
    template_file = open("C:/Users/Jacobs Laptop PC/Documents/AMATRA/AMATRA/AIMS/static/Annual project report template.txt", "r")
    template = template_file.read()
    template_file.close()
    
    test_dict = {
        'projectToggle':True,
    }
    
    report_selector_form = reportSelectorForm(request.POST or None, initial=test_dict)
    context_dict = {'report_selector_form':report_selector_form,}  
    
    all_projects = Project.objects.all()
    context_dict= {
        'All_Projects': all_projects,
    }    
    
    projectObj = Project.objects.get(id=project_ID)
    
    chunks = template.split("//chunk//")
    
    bodyTemplatePt1 = "N/A"
    relatedProjectsTemplate = "N/A"
    bodyTemplatePt2 = "N/A"
    milestoneTemplate = "N/A"
    currentStepTemplate = "N/A"
    futureStepTemplate = "N/A"
    reportsTemplate = "N/A"
    
    for item in chunks:
        name = item[2:item.find("/>")]
        if name == "body_pt1":
            bodyTemplatePt1 = item[item.find("/>")+2:]
        if name == "related_projects":
            relatedProjectsTemplate = item[item.find("/>")+2:]
        elif name == "body_pt2":
            bodyTemplatePt2 = item[item.find("/>")+2:]
        elif name == "milestones":
            milestoneTemplate = item[item.find("/>")+2:]
        elif name == "current_steps":
            currentStepTemplate = item[item.find("/>")+2:]
        elif name == "future_steps":
            futureStepTemplate = item[item.find("/>")+2:]
        elif name == "reports":
            reportsTemplate = item[item.find("/>")+2:] 
            
    all_conMeas_codes = ""
    all_loc_codes = ""
    all_objective_names = ""
    all_objective_descriptions = ""

    for con in projectObj.ConMeas.all():
        try:
            all_conMeas_codes = all_conMeas_codes + con.CMCode + ' '
        except:
            all_conMeas_codes = all_conMeas_codes + " --Empty Conservation Measure-- "
                
    for loc in projectObj.Locations.all():
        try:
            all_loc_codes = all_loc_codes + loc.LocationCode + ", " + loc.LocationName + "; "
        except:
            all_loc_codes = all_loc_codes + " --Empty Location-- "
        
    for obj in projectObj.Objectives.all():
        try:
            all_objective_names = all_objective_names + obj.ObjName + "; "
            all_objective_descriptions = all_objective_descriptions + obj.ObjDescription + "\n"
        except:
            all_objective_names = all_objective_names + " --Empty Objective--; "
            all_objective_descriptions = all_objective_descriptions + " --Empty Objective--\n"
        
    projectLeadName = projectObj.ProjectLead.split(" ")
    try:
        contact = Person.objects.get(LastName = projectLeadName[1])
    except:
        contact = Person(LastName = projectLeadName[1], FirstName = projectLeadName[0],)
        contact.save()
    
    
    report = bodyTemplatePt1.format(project_ID = projectObj.WorktaskID, project_name = projectObj.ProjectName, contact_name = contact.FirstName + " " + contact.LastName, contact_phone = contact.Phone, contact_email = contact.Email, project_start = projectObj.ProjectStart, project_end = projectObj.ProjectEnd, objective_name = all_objective_names , conMeas_name = all_conMeas_codes , location_code = all_loc_codes, obj_description = all_objective_descriptions,)
    
    relatedProjects = RelatedProject.objects.filter(WorktaskID = project_ID)
    
    for related in relatedProjects:
        report = report + relatedProjectsTemplate.format(related_project_ID = related.WorktaskID, related_project_type = related.RelationshipType) +"; "
    
    report_milestones = ""
    report_current = ""
    report_future = ""
    report_outputs = ""
    for obj in projectObj.Objectives.all():
        for mile in obj.Milestones.all():
            all_progresses = ""
            for progress in mile.MilestoneProgress.all():
                try:
                    all_progresses = all_progresses + progress.Description
                except:
                    all_progresses = all_progresses + " --Empty Progress-- "
            report_milestones = report_milestones + milestoneTemplate.format( milestone_description = mile.Description, milestone_progress_description = all_progresses)
    
        for current in Step.objects.filter(StepStartDate__lte = str(datetime.datetime.now().strftime("%Y-%m-%d"))).filter(StepEndDate__gte = str(datetime.datetime.now().strftime("%Y-%m-%d"))):
            report_current = report_current + currentStepTemplate.format(step_code = current.StepCode, step_name = current.StepName, step_summary = current.StepSummary)
        
        for future in Step.objects.filter(StepStartDate__gte = str(datetime.datetime.now().strftime("%Y-%m-%d"))):
            report_future = report_future + futureStepTemplate.format(step_code = future.StepCode, step_name = future.StepName, step_summary = future.StepSummary)
        
    for output in projectObj.Outputs.all():
        report_outputs = report + reportsTemplate.format(output_date = output.OutputDate, output_title = output.OutputTitle)
    
    report = report + bodyTemplatePt2.format(project_summary = projectObj.ProjectSummary, project_background = projectObj.ProjectBackground, year_previous = datetime.datetime.today().year-1, milestones = report_milestones, year_current = datetime.datetime.today().year, current_steps = report_current, year_future = datetime.datetime.today().year+1, future_steps = report_future, reports = report_outputs)
    
    
    report_file = open(os.path.expanduser('~') + '\\Downloads\\' + projectObj.WorktaskID + "_anual_project_report" + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".txt", "w")
    report_file.write(report)
    report_file.close()    
    
    return render(request, 'reports/report_hub.html', context_dict)

@login_required
def generate_report(request, project_ID):
    template_file = open("C:/Users/Jacobs Laptop PC/Documents/AMATRA/AMATRA/AIMS/static/AIMS output template v2.txt", "r")
    template = template_file.read()
    template_file.close()
    
    report_selector_form = reportSelectorForm(request.POST)
    
    projectObj = Project.objects.get(id=project_ID)
    context_dict = {report_selector_form,}
    
    all_projects = Project.objects.all()
    context_dict= {
        'All_Projects': all_projects,
    }
    
    chunks = template.split("//chunk//")
    
    templateTree = "N/A"
    projectTemplate = "N/A"
    projectTriggerTemplate = "N/A"
    triggerStatusTemplate = "N/A"
    projectObjectiveTemplate = "N/A"
    objectiveMilestoneTemplate = "N/A"
    objectiveStepTemplate = "N/A"
    stepMethodTemplate = "N/A"
    methodProtocolTemplate = "N/A"
    outputTemplate = "N/A"
    
    for item in chunks:
        name = item[2:item.find("/>")]
        if name == "template":
            templateTree = item[item.find("/>")+2:]
        if name == "project":
            projectTemplate = item[item.find("/>")+2:]
        elif name == "project_trigger":
            projectTriggerTemplate = item[item.find("/>")+2:]
        elif name == "trigger_status":
            triggerStatusTemplate = item[item.find("/>")+2:]
        elif name == "project_objective":
            projectObjectiveTemplate = item[item.find("/>")+2:]
        elif name == "objective_milestone":
            objectiveMilestoneTemplate = item[item.find("/>")+2:]
        elif name == "objective_step":
            objectiveStepTemplate = item[item.find("/>")+2:]
        elif name == "step_method":
            stepMethodTemplate = item[item.find("/>")+2:]
        elif name == "method_protocol":
            methodProtocolTemplate = item[item.find("/>")+2:]
        elif name == "outputs":
            outputTemplate = item[item.find("/>")+2:]            
    
    all_obj_acryonyms = ""
    all_conMeas_codes = ""
    all_loc_codes = ""
    all_goal_names = ""
    all_related_projects = ""
    
    for obj in projectObj.SpeComs.all():
        all_obj_acryonyms = all_obj_acryonyms + obj.Acronym + ' '
    
    for con in projectObj.ConMeas.all():
        all_conMeas_codes = all_conMeas_codes + con.CMCode + ' '
        
    for loc in projectObj.Locations.all():
        all_loc_codes = all_loc_codes + loc.LocationCode + ' '
        
    for goal in projectObj.Goals.all():
        all_goal_names = all_goal_names + goal.GoalName + ' '
        
    for related in projectObj.RelatedProjects.all():
        all_related_projects = all_related_projects + related.WorktaskID + '\t' + related.RelationshipType + '\n'
    
    report = projectTemplate.format(project_id = projectObj.WorktaskID, project_name = projectObj.ProjectName, time_now = time.asctime( time.localtime(time.time()) ), project_lead = projectObj.ProjectLead, project_contributors = projectObj.ProjectContributors, project_status = projectObj.ProjectStatus, project_type = projectObj.ProjectType, project_startDate = projectObj.ProjectStart, project_endDate = projectObj.ProjectEnd, project_summary = projectObj.ProjectSummary, project_background = projectObj.ProjectBackground, project_speComs = all_obj_acryonyms, project_conMeas = all_conMeas_codes, project_locations = all_loc_codes, project_goals = all_goal_names, project_otherConMeas = projectObj.OtherConsMeas, project_otherSpeComs = projectObj.OtherSpecies, project_relatedProject = all_related_projects)                                    
               
    projectTriggers = Trigger.objects.filter(ProjectID = project_ID)
    triggerNumber = 1
               
    for trigger in projectTriggers:
        if request.POST.get('triggerToggle','') != 'on':
            break
        report = report + projectTriggerTemplate.format(number = triggerNumber, trigger_name = trigger.TriggerName, trigger_description = trigger.TriggerDescription, trigger_indicators = trigger.TriggerIndicators, trigger_response = trigger.ProposedResponse)
        triggerNumber = triggerNumber + 1
        
        triggerStatuses = TriggerStatus.objects.filter(TriggerID = trigger.id)
        
        for status in triggerStatuses:
            if request.POST.get('triggerStatusToggle','') != 'on':
                break
            report = report + triggerStatusTemplate.format(status_trend = status.StatusTrend, status_date = status.ReportingDate, status_interpretation = status.MgmtInterp, status_response = status.MgmtResponse)
     
    projectObjectives = Objective.objects.filter(ProjectID = project_ID)
            
    for objective in projectObjectives:
        if request.POST.get('objectiveToggle','') != 'on':
            break        
        report = report + projectObjectiveTemplate.format(objective_code = objective.ObjCode, objective_name = objective.ObjName, objective_description = objective.ObjDescription, objective_startDate = objective.ObjStartDate, objective_endDate = objective.ObjEndDate, objective_flowDiagram = objective.ObjFlowDiagram)
        
        objectiveMilestones = Milestone.objects.filter(ObjectiveID = objective.id)
        
        for milestone in objectiveMilestones:
            if request.POST.get('milestoneToggle','') != 'on':
                break            
            milestoneProgress = MilestoneProgress.objects.filter(MilestoneID = milestone.id)
            report = report + objectiveMilestoneTemplate.format(milestone_description = milestone.Description, milestone_progress = 'test' '''milestoneProgress.Description''')
            
        objectiveSteps = Step.objects.filter(ObjectiveID = objective.id)
        
        for step in objectiveSteps:
            if request.POST.get('stepToggle','') != 'on':
                break            
            report = report + objectiveStepTemplate.format(step_code = step.StepCode, step_name = step.StepName, step_type = step.StepType, step_summary = step.StepSummary, step_startDate = step.StepStartDate, step_endDate = step.StepEndDate, step_dependancies = step.StepDependencies)
            
            stepMethods = Method.objects.filter(StepID = step.id)
            
            for method in stepMethods:
                if request.POST.get('methodToggle','') != 'on':
                    break                
                report = report + stepMethodTemplate.format(method_code = method.MethodCode, method_title = method.MethodTitle, method_type = method.MethodType, method_date = method.MethodDate, method_version = method.MethodVersion, method_description = method.MethodDescription, method_contact = method.MethodContact)
                
                methodProtocols = Protocol.objects.filter(MethodID = method.id)
                
                for protocol in methodProtocols:
                    if request.POST.get('protocolToggle','') != 'on':
                        break                    
                    report = report + methodProtocolTemplate.format(protocol_tile = protocol.ProtocolTitle, protocol_version = protocol.ProtocolVerision, protocol_date = protocol.ProtocolDate, protocol_author = protocol.ProtocolAuthor, protocol_description = protocol.ProtocolDescription, protocol_link = protocol.ProtocolLink)
                    
    projectOutputs = Output.objects.filter(ProjectID = project_ID)
    print(request.POST.get('outputToggle',''))
    for output in projectOutputs:
        if request.POST.get('outputToggle','') != 'on':
            break
        print('here')
        report = report + outputTemplate.format(output_type = output.OutputType, output_authors = output.OutputAuthors, output_date = output.OutputDate, output_title = output.OutputTitle, output_version = output.OutputVersion, output_description = output.OutputDescription, output_DOI = output.OutputDOI, output_citation = output.OutputCitation, output_URI = output.OutputURI, output_constraints = output.OutputConstraints)
        
    report_file = open(os.path.expanduser('~') + '\\Downloads\\' + projectObj.WorktaskID + "_report_" + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".txt", "w")
    report_file.write(report)
    report_file.close()
    
    return render(request, 'reports/report_hub.html', context_dict)