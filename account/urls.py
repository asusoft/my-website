from django.urls import path, re_path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.home, name='home'),
    path('editCv', views.editCv, name='editCv'),
    path('projects', views.projects, name='projects'),
    path('addProject', views.addProject, name='addProject'),
    path('researches', views.researches, name='researches'),
    path('addResearch', views.addResearch, name='addReserach'),
    path('publications', views.publications, name='publications'),
    path('addPublication', views.addPublication, name='addPublication'),
]