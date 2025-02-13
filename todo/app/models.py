from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.task
    
class History(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.task