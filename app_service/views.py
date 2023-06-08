from django.shortcuts import render

# Create your views here.
def infoService(request):
    return render(request, 'temp/backoffice/service/infoService.html')