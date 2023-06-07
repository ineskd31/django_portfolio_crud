from django.shortcuts import render

# Create your views here.
def skillsInfo(request):
    return render(request, 'temp/backoffice/skills/info.html')