from django.shortcuts import render, redirect
from .models import PortFilter, PortImage
from .forms import PortFilterForm, PortImageForm

# Create your views here.
def infoPort(request):
    allFilter = PortFilter.objects.all()
    allImg = PortImage.objects.all()
    return render(request, 'temp/backoffice/portfolio/infoPort.html', {'allFilter':allFilter, 'allImg':allImg})


def addPortFilter(request):
    if request.method == 'POST':
        form = PortFilterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeback')
    else:
        form = PortFilterForm()
        return render(request, 'temp/backoffice/portfolio/addFilter.html', {'form':form})
    
    
def addPortImage(request):
    if request.method == 'POST':
        form = PortImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeback')
    else:
        form = PortImageForm()
        return render(request, 'temp/backoffice/portfolio/addImage.html', {'form':form})
    
    
    

def deletePortFilter(request, id):
    destroy = PortFilter(id)
    destroy.delete()
    return redirect('homeback')


def deletePortImage(request, id):
    destroy = PortImage(id)
    destroy.delete()
    return redirect('homeback')
