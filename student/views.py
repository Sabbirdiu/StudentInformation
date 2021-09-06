from django.shortcuts import render,redirect
from .models import Student 
from .forms import studentform
from django.http import  HttpResponseRedirect
  
from django.contrib import messages



def home(request):
    stu = Student.objects.all().order_by('stu_id')

    context = {
        'stu':stu
    }
    return render(request,'home.html',context)

def add_student(request):
    stu = studentform()
    if request.method=='POST':
        stu=studentform(request.POST)
        if stu.is_valid():
            stu.save()
            messages.success(request, 'This Student id is added in the list ')
            return redirect('home')
             
        else:
            form = studentform()
           
    context = {
        'stu':stu
    }    
    return render(request, 'add_student.html', context) 