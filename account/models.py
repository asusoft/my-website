from turtle import title
from django.db import models
from django.core.validators import URLValidator
import datetime

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
    picture = models.ImageField(upload_to='pics', default='me.jpg')

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=100)
    abstract = models.TextField()
    topic = models.ManyToManyField(Topic)
    picture = models.ImageField(upload_to='pics', default='me.jpg')
    paper = models.TextField(validators=[URLValidator()])
    repo = models.TextField(validators=[URLValidator()], blank=True, default='#')
    posted = models.DateField(("Date"), default=datetime.date.today)


    class Meta:
        ordering = ['posted']
    
    def __str__(self):
        return self.title