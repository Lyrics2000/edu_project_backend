# Generated by Django 3.2.8 on 2022-01-10 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_scholarship_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='gpa',
            field=models.DecimalField(decimal_places=2, default=0.5, max_digits=20, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0.5)]),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='scholarship_age',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(25), django.core.validators.MinValueValidator(0)]),
        ),
    ]
