# Generated by Django 5.0.4 on 2024-04-22 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answeres', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='AssesmentArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assesment_area_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('full_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=10)),
                ('subject_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sydney_participant', models.IntegerField()),
                ('sydney_percentile', models.IntegerField()),
                ('correct_answer_percentage_per_class', models.FloatField()),
                ('participant', models.IntegerField()),
                ('student_score', models.FloatField()),
                ('year_level_name', models.CharField(max_length=1)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summary_answers', to='data_management.answer')),
                ('assesment_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_management.assesmentarea')),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_management.award')),
                ('correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summary_correct_answers', to='data_management.answer')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_management.school')),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_management.schoolclass')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_management.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_management.subject')),
            ],
        ),
    ]
