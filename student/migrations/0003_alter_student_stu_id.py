# Generated by Django 3.2.7 on 2021-09-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_stu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stu_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]