from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=250)

class Task(models.Model):
    title = models.CharField(max_length=250),
    description = models.TextField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)