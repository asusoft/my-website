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


def topic(request, topic_id):

    try:
        topic = Topic.objects.get(id = topic_id)
    except Project.DoesNotExist:
        return render(request, 'account/404.html')

    articles = Article.objects.all()

    my_articles = []
    for article in articles:
        article_topics = article.topic.all()
        if topic in article_topics:
            my_articles.append(article)

    projects = Project.objects.all()

    my_projects = []
    for project in projects:
        project_topics = project.topic.all()
        if topic in project_topics:
            my_projects.append(project)

    publications = Publication.objects.all()

    my_publications = []
    for publication in publications:
        publication_topics = publication.topic.all()
        if topic in publication_topics:
            my_publications.append(publication)

    return render(request, 'account/topic.html', {'topic': topic, 'articles': my_articles, 'projects': my_projects, 'publications': my_publications})
