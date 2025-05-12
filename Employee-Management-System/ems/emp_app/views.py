from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from django.db.models import Q


from .models import Employee, Department, Role

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'view_all.html',context)

def add_emp(request):
    if request.method == "POST":
        emp_id = request.POST['emp_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])

        new_emp = Employee(emp_id=emp_id,first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added Successfully')
    elif request.method=="GET":
        return render(request,'add_emp.html')
    else:
        return HttpResponse('Something went wrong!....Try again later')

def remove_emp(request,emp_id=None):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return redirect('remove_emp')
        except:
            return HttpResponse("Something went wrong!.....")
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps':emps
        }
        return render(request,'view_all.html',context)
    elif request.method == "GET":
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("Something went wrong!...")



