from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'account/account.html')

def editCv(request):
    return render(request, 'account/editCv.html')

def projects(request):
    return render(request, 'account/projects.html')

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

