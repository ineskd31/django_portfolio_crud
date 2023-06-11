from django.db import models

# Create your models here.
class Contact(models.Model):
    location = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=30)