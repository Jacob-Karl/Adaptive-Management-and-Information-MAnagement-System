# Generated by Django 3.2.4 on 2022-01-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20220118_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='Description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='milestoneprogress',
            name='Description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='milestoneprogress',
            name='ReportingDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='milestoneprogress',
            name='Status',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
