from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def scholarship(request):
    return render(request,'scholarship_list.html')
