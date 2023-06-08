from django.shortcuts import render

# Create your views here.
def infoTesti(request):
    return render(request, 'temp/backoffice/testimonial/infoTesti.html')