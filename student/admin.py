from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stu_id','name', 'age','sex','father_Name','mother_Name','last_Education']
    list_filter = ['stu_id']
admin.site.register(Student,StudentAdmin)
