from django.shortcuts import render
from app_about.models import About
from app_skills.models import Skills
from app_service.models import Service

# Create your views here.
def home(request):
    allabout = About.objects.all()
    allSkills = Skills.objects.all()
    allService = Service.objects.all()
    return render(request, 'temp/home/home.html', {"allabout": allabout, "allSkills":allSkills, "allService": allService})