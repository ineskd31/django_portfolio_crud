from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
def infoContact(request):
    allContact = Contact.objects.all()
    return render(request, 'temp/backoffice/contact/infoContact.html',{'allContact':allContact})



def editContact(request, id):
    edit = Contact.objects.get(id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('homeback')
    else:
        form = ContactForm(instance=edit)
        return render(request, 'temp/backoffice/contact/editContact.html', {'form':form})