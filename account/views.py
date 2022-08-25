from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'account.html')

def editCv(request):
    return render(request, 'editCv.html')

def projects(request):
    return render(request, 'projects.html')

def addProject(request):
    return render(request, 'addProject.html')

def researches(request):
    return render(request, 'researches.html')

def addResearch(request):
    return render(request, 'addResearch.html')

def publications(request):
    return render(request, 'publications.html')

def addPublication(request):
    return render(request, 'addPublication.html')

