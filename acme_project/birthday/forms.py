from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'
        widget = {'birthday': forms.DateInput(attrs={'type': 'date'})        
        }
        