# Generated by Django 3.2.8 on 2021-11-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20211127_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarship',
            name='scholarship_description',
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='deadline_apply',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='deadline_review',
            field=models.DateField(),
        ),
    ]
