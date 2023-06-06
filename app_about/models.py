from django.db import models

# Create your models here.
class About(models.Model):
    intro = models.TextField
    birthday = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    phone = models.CharField()
    city = models.CharField(max_length=50)
    
    age = models.PositiveIntegerField()
    degree = models.CharField()
    email = models.EmailField()
    freelance = models.char
    
    