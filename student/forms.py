from django import forms
from .models import *
from django.forms import fields

class studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'