# Generated by Django 3.2.8 on 2021-10-31 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resume_letter', models.FileField(upload_to=mainapp.models.upload_file_path)),
                ('extra_notes_resume', models.TextField()),
                ('recommendation_letter', models.FileField(upload_to=mainapp.models.upload_file_path)),
                ('etra_notes_rec_letter', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class_name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application_status', models.BooleanField(default=False)),
                ('application_etra_notes', models.TextField()),
                ('application_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.application')),
                ('commitee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolAttended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('school_name', models.CharField(max_length=255)),
                ('school_type', models.CharField(max_length=255)),
                ('final_performance', models.CharField(max_length=255)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('scholarship_name', models.CharField(max_length=255)),
                ('school_name', models.CharField(max_length=255)),
                ('deadline_apply', models.DateTimeField()),
                ('deadline_review', models.DateTimeField()),
                ('scholarship_details', models.TextField()),
                ('web_link', models.URLField()),
                ('scholarship_budget', models.DecimalField(decimal_places=2, max_digits=20)),
                ('scholarship_type', models.CharField(max_length=255)),
                ('scholarship_country', models.CharField(max_length=255)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('response_text', models.TextField()),
                ('feedback_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.feedback')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('permanent_address', models.CharField(max_length=255)),
                ('current_address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employer_name', models.CharField(max_length=255)),
                ('employer_address', models.CharField(max_length=255)),
                ('employer_designation', models.CharField(max_length=255)),
                ('employer_phone', models.CharField(max_length=255)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='application',
            name='scholarship_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.scholarship'),
        ),
        migrations.AddField(
            model_name='application',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
