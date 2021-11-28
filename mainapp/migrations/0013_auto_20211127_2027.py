# Generated by Django 3.2.8 on 2021-11-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20211127_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='scholarship_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='deadline_apply',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='deadline_review',
            field=models.DateTimeField(),
        ),
    ]