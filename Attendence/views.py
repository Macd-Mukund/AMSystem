
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .models import Attendance_Record,Employee_Record
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    return render(request,'Home.html')

def HRloginform(request):
    return render(request,'HRlogin.html')    

def Employeeloginform(request):
    return render(request,'Employeelogin.html')

def HRlogin(request):
    if request.method == "POST":
        usernm = request.POST.get('username')
        passwd = request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=usernm,password=passwd) 
        if user is not None:
            login(request, user)
            messages.success(request,"User successfully Logged In ! Now you can Access Current Application ......")
            stud = Employee_Record.objects.all()
            record = Attendance_Record.objects.all()
            return render(request,'HRprofile.html', {'stu': stud , 'record': record } )
        else:
            messages.error(request, 'User login failed ! Please Enter correct credentials')
            return redirect('/')
    return render(request,'HRprofile.html')



def HRlogout(request):
        logout(request)
        messages.success(request, "User successfully Logged Out ! Please Re_Login for Access again .....")
        return redirect('HRloginform')

        
def Employeelogin(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee-id')
        password = request.POST.get('employee-password')
        employee =Employee_Record.objects.get(Employee_Id__exact = employee_id, Password__exact = password )
        if employee is not None:
            epid=employee.Employee_Id
            record=Attendance_Record.objects.filter(Employee_Id__exact = epid)
            return render(request,'Employeeprofile.html', {'employee':employee,'record':record})
        return redirect('/')
            

def Attendan(request):
    if request.method == 'POST':
        empid = request.POST.get('emp-id')
        empname = request.POST.get('emp-name')
        atten = request.POST.get('attendance')
        clockin = request.POST.get('clockin')
        
        extra= request.POST.get('extrahour')
        details= Attendance_Record(Employee_Id=empid,Employee_Name=empname,Attendance=atten, Clockin = clockin , Clockout = datetime.today() ,Extrahours=extra)
        details.save()
        messages.success(request, 'Attendance Successfully !')

    return render(request,"Employeeprofile.html")    

def Addemployee(request):
    if request.method == 'POST':
        empid = request.POST.get('emp-id')
        empname = request.POST.get('emp-name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        design= request.POST.get('design')
        passd= request.POST.get('password')
        details= Employee_Record(Employee_Id=empid,Employee_Name=empname,Phone_No = phone, Email=email, Designation = design,Password=passd)
        details.save()
        messages.success(request, 'Attendance Successfully !')

    return redirect('HRloginform')           


    
    

