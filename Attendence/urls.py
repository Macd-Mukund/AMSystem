from django.contrib import admin
from django.urls import path
from .import views
#from .views import Update

urlpatterns = [
    path('',views.home,name="home"),
    path('HRloginform',views.HRloginform,name="HRloginform"),
    path('Employeeloginform',views.Employeeloginform,name="Employeeloginform"),

    path('HRlogin',views.HRlogin,name="HRlogin"),
    path('HRlogout',views.HRlogout,name="HRlogout"),
    path('Employeelogin',views.Employeelogin,name="Employeelogin"),

    path('Attendan',views.Attendan,name="Attendan"),
    path('Addemployee',views.Addemployee,name="Addemployee"),

    ]
