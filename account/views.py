from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    persona = Resume.objects.first
    projects = Project.objects.all()
    return render(request, 'account/index.html', {'persona': persona, 'projects': projects})

def editCv(request):
    return render(request, 'account/editCv.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'account/projects.html', {'projects': projects})

def addProject(request):
    return render(request, 'account/addProject.html')

def researches(request):
    return render(request, 'account/researches.html')

def addResearch(request):
    return render(request, 'account/addResearch.html')

def publications(request):
    return render(request, 'account/publications.html')

def addPublication(request):
    return render(request, 'account/addPublication.html')

