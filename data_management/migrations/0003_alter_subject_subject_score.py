# Generated by Django 5.0.4 on 2024-04-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0002_rename_model_name_award_award_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_score',
            field=models.FloatField(default=None),
        ),
    ]
