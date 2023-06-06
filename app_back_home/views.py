from django.shortcuts import render
from app_about.models import About

# Create your views here.
def backhome(request):
    allabout = About.objects.all()
    return render(request, 'temp/backoffice/backHome.html', {"allabout": allabout})