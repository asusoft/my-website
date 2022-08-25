from turtle import title
from django.db import models
from django.core.validators import URLValidator

# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    picture = models.ImageField(upload_to='pics')
    cv = models.TextField(validators=[URLValidator()])


class Topic(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    topic = models.ManyToManyField(Topic)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title