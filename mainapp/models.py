from django.db import models
from django.db.models.base import Model
from authentification.models import User
import os
import random

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_file_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "thumbnails/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.

class Classes(BaseModel):
    class_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.class_name


class ExtraInfo(BaseModel):
    student_id = models.ForeignKey(User,on_delete=models.CASCADE)
    permanent_address =  models.CharField(max_length=255)
    current_address =  models.CharField(max_length=255)
    country =  models.CharField(max_length=255)
    date_of_birth =  models.DateField()

    def __str__(self):
        return self.permanent_address

class EmployerDetails(BaseModel):
    student_id = models.ForeignKey(User,on_delete=models.CASCADE)
    employer_name =  models.CharField(max_length=255)
    employer_address =  models.CharField(max_length=255)
    employer_designation =  models.CharField(max_length=255)
    employer_phone = models.CharField(max_length=255)

    def __str__(self):
        return self.employer_name


class SchoolAttended(BaseModel):
    student_id = models.ForeignKey(User,on_delete=models.CASCADE)
    school_name =  models.CharField(max_length=255)
    school_type =  models.CharField(max_length=255)
    final_performance =  models.CharField(max_length=255)

    def __str__(self):
        return self.school_name

class Scholarship(BaseModel):
    admin_id = models.ForeignKey(User,on_delete=models.CASCADE)
    scholarship_name =  models.CharField(max_length=255)
    school_name =  models.CharField(max_length=255)
    deadline_apply =  models.DateTimeField()
    deadline_review =  models.DateTimeField()
    scholarship_details =  models.TextField()
    web_link =  models.URLField()
    scholarship_budget =  models.DecimalField(max_digits=20,decimal_places=2)
    scholarship_type =  models.CharField(max_length=255)
    scholarship_country =  models.CharField(max_length=255)

    def __str__(self):
        return self.school_name


class Application(BaseModel):
    scholarship_id =  models.ForeignKey(Scholarship,on_delete=models.CASCADE)
    student_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    resume_letter =  models.FileField(upload_to=upload_file_path)
    extra_notes_resume =  models.TextField()
    recommendation_letter =  models.FileField(upload_to=upload_file_path)
    etra_notes_rec_letter = models.TextField()

    def __str__(self):
        return str(self.student_id)


class Feedback(BaseModel):
    commitee_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    application_id =  models.ForeignKey(Application,on_delete=models.CASCADE)
    application_status =  models.BooleanField(default=False)
    application_etra_notes  = models.TextField()

    def __str__(self):
        return str(self.commitee_id)

class Response(BaseModel):
    feedback_id =  models.ForeignKey(Feedback,on_delete=models.CASCADE)
    response_text =  models.TextField()

    def __str__(self):
        return str(self.feedback_id)
 


