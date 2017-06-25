from django.db import models

# Create your models here.
class Todolist(models.Model):
    event = models.CharField(max_length=300)
    status = models.CharField(max_length=50)

