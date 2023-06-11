from django.shortcuts import render
from app_about.models import About
from app_skills.models import Skills
from app_service.models import Service
from app_testimonials.models import Testi
from app_portfolio.models import PortFilter, PortImage
from app_contact.models import Contact


# Create your views here.
def backhome(request):
    allabout = About.objects.all()
    allSkills = Skills.objects.all()
    allService = Service.objects.all()
    allTesti = Testi.objects.all()
    allFilter = PortFilter.objects.all()
    allImg = PortImage.objects.all()
    allContact = Contact.objects.all()
    
    return render(request, 'temp/backoffice/backHome.html', {"allabout": allabout, "allSkills":allSkills, "allService":allService, "allTesti": allTesti, "allFilter":allFilter, "allImg":allImg, "allContact":allContact})

