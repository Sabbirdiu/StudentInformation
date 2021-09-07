from django.shortcuts import render,redirect
from .models import Student 
from .forms import studentform
from django.http import  HttpResponseRedirect
  
from django.contrib import messages
from django.shortcuts import get_object_or_404


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

# update view for details
def update_view(request, id):

    

    obj = get_object_or_404(Student, id = id)

    form = studentform(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form' : form
    }
    return render(request, "update_view.html", context)