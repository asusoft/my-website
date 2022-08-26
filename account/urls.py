from django.urls import path, re_path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.home, name='home'),
    path('editCv', views.editCv, name='editCv'),
    path('projects', views.projects, name='projects'),
    path('viewProject/<int:project_id>', views.viewProject, name='viewProject'),
    path('researches', views.researches, name='researches'),
    path('viewResearch', views.viewResearch, name='viewReserach'),
    path('publications', views.publications, name='publications'),
]