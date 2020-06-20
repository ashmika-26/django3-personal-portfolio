from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):

    return render(request,'portfolio/home.html')

def about(request):
    return render(request,'portfolio/about.html')

def project(request):
    projects=Project.objects.all()
    return render(request,'portfolio/project.html',{'projects':projects})
