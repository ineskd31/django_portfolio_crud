from django.db import models

# Create your models here.
class PortFilter(models.Model):
    name = models.CharField(max_length=50)




class PortImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=500)