# Generated by Django 5.1.2 on 2024-10-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff_app", "0002_student_dob_student_name_student_school"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coustomuser",
            name="roll_number",
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="name",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name="student",
            name="roll_number",
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
