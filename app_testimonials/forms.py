from django import forms
from .models import Testi

class TestiForm(forms.ModelForm):
    class Meta:
        model = Testi
        fields = '__all__'