# Generated by Django 3.2.4 on 2021-09-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_functions', '0005_auto_20210903_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
