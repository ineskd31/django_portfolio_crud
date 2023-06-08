from django.shortcuts import render,redirect
from .models import Skills
from .forms import SkillsForm

# Create your views here.


def skillsInfo(request):
    all = Skills.objects.all()
    return render(request, 'temp/backoffice/skills/info.html', {"all":all})


def skillsEdit(request, id):
    edit = Skills.objects.get(id=id)
    if request.method == 'POST':
        form = SkillsForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('homeback')
    else:
        form = SkillsForm(instance=edit)
        return render(request, 'temp/backoffice/skills/edit.html', {"form":form})
    
    
    
def delete(request, id):
    destroy = Skills(id)
    destroy.delete()
    return redirect('homeback')


def ajouter(request):
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeback')
    else:
        form = SkillsForm()
        return render(request, 'temp/backoffice/skills/ajouter.html', {'form':form})