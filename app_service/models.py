from django.db import models

# Create your models here.
class Service(models.Model):
    
    ICON_CHOICES = (
        ("bi-briefcase", "bi bi-briefcase"),
        ("bi-card-checklist", "bi-card-checklist"),
        ("bi-bar-chart", "bi bi-bar-chart"),
        ("bi-binoculars", "bi bi-binoculars"),
        ("bi-brightness-high", "bi bi-brightness-high"),
        ("bi-calendar4-week", "bi bi-calendar4-week"),
    )
    
    
    titre = models.CharField(max_length=60)
    description = models.TextField()
    icon = models.CharField(max_length=80, choices=ICON_CHOICES)