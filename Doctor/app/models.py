import datetime
from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to ='pics')
    Short_descr = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
