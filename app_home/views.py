from django.shortcuts import render
from app_about.models import About

# Create your views here.
def home(request):
    allabout = About.objects.all()
    return render(request, 'temp/home/home.html', {"allabout": allabout})