from django import forms
from django.forms import ModelForm, CharField
from .models import *
from django.forms import fields
from crispy_forms.helper import FormHelper
class studentform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(studentform, self).__init__(*args, **kwargs)
    
        self.fields['stu_id'].label = "Student Id"
        self.fields['name'].label =  "Student Name"
        self.fields['age'].label = "Age"
        self.fields['sex'].label = "Sex"
        self.fields['father_Name'].label = "Father Name"
        self.fields['mother_Name'].label = "Mother Name"
        self.fields['last_Education'].label = "Last Education"

        self.fields['stu_id'].widget.attrs.update(
            {
                'placeholder': 'ex:171-15-8767',
            }
        )
        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Enter Full Name',
            }
        )
        # self.fields['age'].widget.attrs.update(
        #     {
        #         'placeholder': 'Enter Age',
        #     }
        # )
        # self.fields['sex'].widget.attrs.update(
        #     {
        #         'placeholder': 'Sex',
        #     }
        # )
        # self.fields['father_Name'].widget.attrs.update(
        #     {
        #         'placeholder': 'Father Name',
        #     }
        # )
        # self.fields['mother_Name'].widget.attrs.update(
        #     {
        #         'placeholder': 'Mother Name',
        #     }
        # )
        self.fields['last_Education'].widget.attrs.update(
            {
                'placeholder': 'ex: Daffodil International University',
            }
        )
 
    class Meta:
        model = Student
        fields = '__all__'
 
