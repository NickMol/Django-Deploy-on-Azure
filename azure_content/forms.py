from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, DateInput, TimeInput
from.models import *

class ProjectForm(forms.ModelForm):
    name =  forms.CharField(label="Name",required=True)
    description = forms.CharField(label="Description", required=False,help_text="", widget=forms.Textarea(attrs={'rows': 10, 'cols': 85}))
    class Meta: 
        model = Project
        fields = ['name', 'description']  