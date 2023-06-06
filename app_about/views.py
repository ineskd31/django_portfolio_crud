from django.shortcuts import render,redirect
from .models import About
from .forms import AboutForm


# Create your views here.
def edit(request, id):
    edit = About.objects.get(id=id)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('homeback')
    else:
        form = AboutForm(instance=edit)
        return render(request, 'temp/backoffice/about/edit.html', {'form':form})