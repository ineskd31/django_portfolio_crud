from django.db import models

# Create your models here.
class Testi(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=100)
    citation = models.TextField()
    image = models.CharField(max_length=700)