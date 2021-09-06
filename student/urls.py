
from django.urls import path
from django.urls import path
from .views import home,add_student
urlpatterns = [
    path('', home,name="home"),
    path('add/', add_student,name="add_student"),
]
