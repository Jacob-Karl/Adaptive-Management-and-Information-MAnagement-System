# Generated by Django 3.2.4 on 2021-12-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20211214_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='OtherConsMeas',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='OtherSpecies',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectBackground',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectEnd',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectLead',
            field=models.CharField(max_length=38, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectName',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectStart',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectStatus',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectSummary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectType',
            field=models.CharField(choices=[('Fish Augmentation', 'Fish Augmentation'), ('Species Research', 'Species Research'), ('System Monitoring', 'System Monitoring'), ('Conservation Area Development and Management', 'Fish Augmentation'), ('Post-Development Monitoring', 'Post-Development Monitoring'), ('Adaptive Management Program', 'Adaptive Management Program')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='WorktaskID',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
