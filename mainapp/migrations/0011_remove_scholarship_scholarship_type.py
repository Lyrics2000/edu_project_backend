# Generated by Django 3.2.8 on 2021-11-27 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_scholarship_gpa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarship',
            name='scholarship_type',
        ),
    ]
