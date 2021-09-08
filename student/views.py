from django.shortcuts import render,redirect
from .models import Student 
from .forms import studentform
from django.http import  HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    stu = Student.objects.order_by('stu_id')
    paginator = Paginator(stu, 6)
    page = request.GET.get('page')
    paged_listings  = paginator.get_page(page)
    
    context = {
        'listings':paged_listings,
    }
    return render(request,'home.html',context)
@permission_required('auth.view_user')
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
@permission_required('auth.view_user')
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
# delete view for details
@permission_required('auth.view_user')
def delete_view(request, id):
    context ={}
    obj = get_object_or_404(Student, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        return redirect("home")
 
    return render(request, "delete_view.html", context)