# Generated by Django 5.0.7 on 2024-10-07 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0002_studentlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('AOOP', 'Advanced object-oriented Programming'), ('PFSD', 'Python Full Stack Development')], max_length=50)),
                ('section', models.CharField(choices=[('S11', 'SECTION S11'), ('S12', 'SECTION S12'), ('S13', 'SECTION S13'), ('S14', 'SECTION S14'), ('S15', 'SECTION S15')], max_length=50)),
                ('StudentList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentlist')),
            ],
        ),
    ]