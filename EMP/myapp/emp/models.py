from django.db import models

# Create your models here.

class emp(models.Model):
    name= models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    position = models.CharField(max_length=150)
    department=models.CharField(max_length=10)