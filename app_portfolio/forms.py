from django import forms
from .models import PortFilter, PortImage


class PortFilterForm(forms.ModelForm):
    class Meta:
        model = PortFilter
        fields = '__all__'
        






class PortImageForm(forms.ModelForm):
    
    name = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(PortImageForm, self).__init__(*args, **kwargs)
        self.fields['name'].choices = self.get_choices()

    def get_choices(self):
        datas = PortFilter.objects.values_list('name', flat=True)

        choices = [(data, data) for data in datas]

        return choices
    
    class Meta:
        model = PortImage
        fields = '__all__'