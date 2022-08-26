from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def home(request):
    persona = Resume.objects.first
    projects = Project.objects.all()
    publications = Publication.objects.all()
    articles = Article.objects.all()
    return render(request, 'account/index.html', {'persona': persona, 'projects': projects, 'articles': articles, 'publications': publications})

def editCv(request):
    return render(request, 'account/editCv.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'account/projects.html', {'projects': projects})

def viewProject(request, project_id):

    try:
        project = Project.objects.get(id = project_id)
    except Project.DoesNotExist:
        return render(request, 'account/404.html')

    return render(request, 'account/viewProject.html', {'project': project})

def researches(request):
    return render(request, 'account/researches.html')

def viewResearch(request):
    return render(request, 'account/viewResearch.html')

def publications(request):
    publications = Publication.objects.all()
    return render(request, 'account/publications.html', {'publications': publications})


