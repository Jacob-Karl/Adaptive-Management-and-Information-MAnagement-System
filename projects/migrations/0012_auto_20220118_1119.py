# Generated by Django 3.2.4 on 2022-01-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20220113_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triggerstatus',
            name='MgmtInterp',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='triggerstatus',
            name='MgmtResponse',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='triggerstatus',
            name='ReportingDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='triggerstatus',
            name='StatusTrend',
            field=models.TextField(null=True),
        ),
    ]
