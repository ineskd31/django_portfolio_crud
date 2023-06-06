from django.shortcuts import render

# Create your views here.
def backhome(request):
    return render(request, 'temp/backoffice/backHome.html')