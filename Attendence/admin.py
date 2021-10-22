from django.contrib import admin
from .models import Employee_Record,Attendance_Record

# Register your models here.
admin.site.register(Employee_Record)
admin.site.register(Attendance_Record)
