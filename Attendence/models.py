from django.db import models
from django.db.models.fields import DateField


# Create your models here.
class Employee_Record(models.Model):
    Employee_Id = models.IntegerField()
    Employee_Name = models.CharField(max_length=30 ,default='Name')
    Designation = models.CharField(max_length=20)
    Email = models.EmailField(max_length=40)
    Phone_No = models.CharField(max_length=10)
    Password = models.CharField(max_length=40)

    def __str__(self) :
        return (self.Employee_Name)

# Create your models here.
class Attendance_Record(models.Model):
    Employee_Id = models.IntegerField()
    Employee_Name = models.CharField(max_length=30 ,default='Name')
    Extrahours = models.IntegerField()
    Attendance = models.CharField(max_length=50)
    Clockin = models.DateTimeField()
    Clockout = models.DateTimeField()

    def __str__(self):
        return (self.Employee_Name)

# Create your models here.
