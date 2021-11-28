from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from account.models import User
from .models import (
    Slider,
    Scholarship,
    AboutSection,
    UserProfile
)

# Create your views here.
def index(request):
    all_slider =  Slider.objects.all()
    all_scholarship =  Scholarship.objects.all()

    context = {
        'all_slider' :  all_slider,
        'all_scholarship' : all_scholarship
    }
    return render(request,'index.html',context)


def about(request):
    about =  AboutSection.objects.first()
    context = {
        'about' :  about
    }
    return render(request,'about.html',context)


def scholarship(request):
    all_scholarship =  Scholarship.objects.all()
    context = {

        'all_scholarship' : all_scholarship

    }
    return render(request,'scholarship_list.html',context)


@login_required(login_url="account:sign_in")
def user_profile(request):
    try:
        user_id =  request.user.id
        user_obj =  User.objects.get(id =  user_id)
        user_profile_obj =  UserProfile.objects.get(user_id =  user_obj)

        context = {
            'user_profile' :  user_profile_obj
        }
        return render(request,'profile.html',context)
    except UserProfile.DoesNotExist:
        context = {
            'user_profile' :  None
        }

        return render(request,'profile.html',context)


@login_required(login_url="account:sign_in")
def edit_profile(request):
    if request.method == "POST":
        user_id =  request.user.id
        country =  request.POST.get("country")
        permanent_address =  request.POST.get("permanent_address")
        current_address =  request.POST.get("current_address")
        scholarship_type =  request.POST.get("type")
        user_image =  request.FILES['scholarship_img']
        
        user_obj =  User.objects.get(id =  user_id)
        user_profile_obj,created =  UserProfile.objects.get_or_create(user_id = user_obj)
        user_profile_obj.country =  country
        user_profile_obj.permanent_address =  permanent_address
        user_profile_obj.physical_address =  current_address
        user_profile_obj.scholarship_type =  scholarship_type
        user_profile_obj.image =  user_image
        user_profile_obj.save()
        return redirect("mainapp:user_profile")

    try:
        user_id =  request.user.id
        user_obj =  User.objects.get(id =  user_id)
        user_profile_obj =  UserProfile.objects.get(user_id =  user_obj)

        context = {
            'user_profile' :  user_profile_obj
        }
        return render(request,'edit_profile.html',context)
    except UserProfile.DoesNotExist:
        context = {
            'user_profile' :  None
        }

        return render(request,'edit_profile.html',context)

    


@login_required(login_url="account:sign_in")
def upload_scholarship(request):
    if request.method == "POST":
        user_id  =  request.user.id
        scholarship_name =  request.POST.get("scholarship_name")
        school_name =  request.POST.get("school_name")
        deadline_apply =  request.POST.get("deadline_to_apply")
        deadline_to_review =  request.POST.get("deadline_to_review")
        scholarship_details = request.POST.get("scholarship_details")
        web_link =  request.POST.get("web_link"),
        scholarship_budget =  request.POST.get("scholarship_budget")
        scholarship_type =  request.POST.get("scholarship_type")
        scholarship_country = request.POST.get("scholarship_country")
        gpa =  request.POST.get("gpa")
        scholarship_age_limit =  request.POST.get("scholarship_age_limit")
        scholarship_employment = request.POST.get("scholarship_employment_status")
        scholarship_thumbnail =  request.FILES['scholarship_image']
        course =  request.POST.get("course")
        user_obj =  User.objects.get(id =  user_id)
        if scholarship_employment == "on":
        
            Scholarship.objects.create(
                admin_id =  user_obj,
                scholarship_name = scholarship_name,
                school_name = school_name,
                deadline_apply = deadline_apply,
                deadline_review = deadline_to_review,
                course =  course,
                scholarship_details =  scholarship_details,
                web_link = web_link,
                scholarship_budget = float(scholarship_budget),
                scholarship_type = scholarship_type,
                scholarship_country = scholarship_country,
                gpa = gpa,
                scholarship_age = scholarship_age_limit,
                scholarship_employment =  True,
                scholarship_thumbnail = scholarship_thumbnail

            )

        else:
            Scholarship.objects.create(
                admin_id =  user_obj,
                scholarship_name = scholarship_name,
                school_name = school_name,
                deadline_apply = deadline_apply,
                deadline_review = deadline_to_review,
                course =  course,
                scholarship_details =  scholarship_details,
                web_link = web_link,
                scholarship_budget = float(scholarship_budget),
                scholarship_type = scholarship_type,
                scholarship_country = scholarship_country,
                gpa = gpa,
                scholarship_age = scholarship_age_limit,
                scholarship_employment =  True,
                scholarship_thumbnail = scholarship_thumbnail

            )

        
    return render(request,'upload_scholarship.html')


@login_required(login_url="account:sign_in")
def recommendations(request):
    scholarships = Scholarship.objects.all()
    context = {
        'scholarships' :  scholarships
    }
    if request.method ==  "POST":
        employment_status =  request.POST.get("employment_status")
        course =  request.POST.get("course")
        gpa_score =  request.POST.get("gpa_score")
        age =  request.POST.get("age")
        country =  request.POST.get("country")
        scholarship_budget =  request.POST.get("scholarship_budget")
        scholarship_type =  request.POST.get("scholarship_type")
        if employment_status == 'on':
            print("starting...")
            perfect_filtered_scholarships =  Scholarship.objects.filter(scholarship_employment =True,
            course =  course,
            gpa = gpa_score,
            scholarship_age = age,
            scholarship_country = country,
            scholarship_budget = scholarship_budget,
            scholarship_type = scholarship_type )

           

            fifty_percent_filtered = Scholarship.objects.filter(scholarship_employment =True,
            course =  course,
            gpa = gpa_score,
            scholarship_budget = scholarship_budget,
            )

            zero_percent_filtered_scholarships =  Scholarship.objects.filter(~Q(scholarship_employment =True,
            course =  course,
            gpa = gpa_score,
            scholarship_age = age,
            scholarship_country = country,
            scholarship_budget = scholarship_budget,
            scholarship_type = scholarship_type ))

            print(perfect_filtered_scholarships)


            context = {
                'perfect_filtered_scholarships' : perfect_filtered_scholarships,
                'seventy_percent_filtered' : fifty_percent_filtered,
                'zero_percent_filtered_scholarships' : zero_percent_filtered_scholarships
            }

            return render(request,'scholarship_filter.html',context)

        else:
            print("starting...")
            perfect_filtered_scholarships =  Scholarship.objects.filter(scholarship_employment =False,
            course =  course,
            gpa = gpa_score,
            scholarship_age = age,
            scholarship_country = country,
            scholarship_budget = scholarship_budget,
            scholarship_type = scholarship_type )

           

            fifty_percent_filtered = Scholarship.objects.filter(scholarship_employment =False,
            course =  course,
            gpa = gpa_score,
            scholarship_budget = scholarship_budget,
            )

            zero_percent_filtered_scholarships =  Scholarship.objects.filter(~Q(scholarship_employment =False,
            course =  course,
            gpa = gpa_score,
            scholarship_age = age,
            scholarship_country = country,
            scholarship_budget = scholarship_budget,
            scholarship_type = scholarship_type ))

            print(perfect_filtered_scholarships)


            context = {
                'perfect_filtered_scholarships' : perfect_filtered_scholarships,
                'seventy_percent_filtered' : fifty_percent_filtered,
                'zero_percent_filtered_scholarships' : zero_percent_filtered_scholarships
            }

            return render(request,'scholarship_filter.html',context)

    return render(request,'recommendations.html',context)
