# Generated by Django 3.2.4 on 2021-12-17 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scopes', '0007_alter_speciescommunity_picture'),
        ('user_functions', '0007_contributor'),
        ('projects', '0006_auto_20211216_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='method',
            name='Protocols',
        ),
        migrations.AddField(
            model_name='method',
            name='Protocols',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.protocol'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='MilestoneProgress',
        ),
        migrations.AddField(
            model_name='milestone',
            name='MilestoneProgress',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.milestoneprogress'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='objective',
            name='Milestones',
        ),
        migrations.AddField(
            model_name='objective',
            name='Milestones',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.milestone'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='objective',
            name='Steps',
        ),
        migrations.AddField(
            model_name='objective',
            name='Steps',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.step'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='ConMeas',
        ),
        migrations.AddField(
            model_name='project',
            name='ConMeas',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='scopes.conservationmeasure'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='Goals',
        ),
        migrations.AddField(
            model_name='project',
            name='Goals',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='scopes.goal'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='Locations',
        ),
        migrations.AddField(
            model_name='project',
            name='Locations',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='scopes.location'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='Objectives',
        ),
        migrations.AddField(
            model_name='project',
            name='Objectives',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.objective'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='Outputs',
        ),
        migrations.AddField(
            model_name='project',
            name='Outputs',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.output'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='People',
        ),
        migrations.AddField(
            model_name='project',
            name='People',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user_functions.person'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='ProjectContributors',
        ),
        migrations.AddField(
            model_name='project',
            name='ProjectContributors',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user_functions.contributor'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='RelatedProjects',
        ),
        migrations.AddField(
            model_name='project',
            name='RelatedProjects',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.relatedproject'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='SpeComs',
        ),
        migrations.AddField(
            model_name='project',
            name='SpeComs',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='scopes.speciescommunity'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='Triggers',
        ),
        migrations.AddField(
            model_name='project',
            name='Triggers',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.trigger'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='step',
            name='Methods',
        ),
        migrations.AddField(
            model_name='step',
            name='Methods',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.method'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='trigger',
            name='TriggerStatus',
        ),
        migrations.AddField(
            model_name='trigger',
            name='TriggerStatus',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.triggerstatus'),
            preserve_default=False,
        ),
    ]
