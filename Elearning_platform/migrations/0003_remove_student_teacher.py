# Generated by Django 4.1.5 on 2023-02-01 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_platform', '0002_student_course_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
