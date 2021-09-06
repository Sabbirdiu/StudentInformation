from django.shortcuts import render

# Create your views here.
from .models import Student 

def home(request):
    stu = Student.objects.all().order_by('stu_id')

    context = {
        'stu':stu
    }
    return render(request,'home.html',context)