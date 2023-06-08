from django.shortcuts import render,redirect
from .models import Service
from .forms import ServiceForm

# Create your views here.
def infoService(request):
    allService = Service.objects.all()
    return render(request, 'temp/backoffice/service/infoService.html', {"allService":allService})


def deleteService(request, id):
    destroy = Service(id)
    destroy.delete()
    return redirect('homeback')



def addService(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeback')
    else:
        form = ServiceForm()
        return render(request, 'temp/backoffice/service/addService.html', {'form':form})
    
    
    
    def editService(request, id):
        edit = Service.objects.get(id=id)
        if request.method == 'POST':
            form = ServiceForm(request.POST, instance=edit)
            if form.is_valid():
                form.save()
                return redirect('homeback')
        else:
            form = ServiceForm(instance=edit)
            return render(request, 'temp/backoffice/service/editService.html', {'form':form})
                
