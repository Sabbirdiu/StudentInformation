
from django.urls import path
from django.urls import path
from .views import home,add_student,update_view,delete_view
urlpatterns = [
    path('', home,name="home"),
    path('add/', add_student,name="add_student"),
    path('<id>/update_view/', update_view,name="update_view"),
    path('<id>/delete', delete_view,name="delete_view" ),

]
