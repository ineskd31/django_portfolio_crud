from django.shortcuts import render, redirect
from .models import Testi
from .forms import TestiForm


# Create your views here.
def infoTesti(request):
    allTesti = Testi.objects.all()
    return render(request, 'temp/backoffice/testimonial/infoTesti.html', {'allTesti':allTesti})


def addTesti(request):
    if request.method == 'POST':
        form = TestiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeback')
    else:
        form = TestiForm()
        return render(request, 'temp/backoffice/testimonial/addTesti.html', {'form':form})


def editTesti(request, id):
    edit = Testi.objects.get(id=id)
    if request.method == 'POST':
        form = TestiForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('homeback')
    else:
        form = TestiForm(instance=edit)
        return render(request, 'temp/backoffice/testimonial/editTesti.html', {'form':form})
    
    
    
def deleteTesti(request, id):
    destroy = Testi(id)
    destroy.delete()
    return redirect('homeback')

