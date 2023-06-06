from django.db import models

# Create your models here.
class About(models.Model):
    intro = models.TextField()
    
    birthday = models.CharField(max_length=30)
    website = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=50)
    email = models.EmailField()
    freelance = models.CharField(max_length=50)
    
    description = models.TextField()
    
    
    