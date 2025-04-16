from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import emp

# Create your views here.
def emp_home(request):
    # return HttpResponse("studnet hoe page")
    return render(request,"./emp/home.html")

def View_Employees(request):
    emps=emp.objects.all()
    print(emps)
    return render(request,"emp/view.html",{
        'emps':emps
    })


def Add_Employee(request):
    if request.method=="POST":
        print("data is coiming ")
        # data fach
        
        emp_name = request.POST.get("name")
        emp_email = request.POST.get("email")
        emp_position = request.POST.get("position")
        emp_department = request.POST.get("department")
          
        # create model object and sat the data
        e=emp()
        e.name=emp_name
        e.email=emp_email
        e.position=emp_position
        e.department=emp_department
       
        #  save  the data
        e.save()
        
        
        
        
        
        return redirect("/emp/home/")
    
    return render(request,"emp/add.html")

def Edit_Employee(request,emp_id):
    Emp=emp.objects.get(pk=emp_id)
    
    
    return render(request,"emp/edit.html",{
        'emp':Emp
    })

def Delete_Employee(request,emp_id):
    Emp = emp.objects.get(pk=emp_id)
    Emp.delete()
    return redirect("/emp/home/")

def logout(request):
    return render(request,"./emp/login.html")


def do_update(request,emp_id):
    if request.method=="POST":
        # fach data
        
        emp_name = request.POST.get("name")
        emp_email = request.POST.get("email")
        emp_position = request.POST.get("position")
        emp_department = request.POST.get("department")
        
        e=emp.objects.get(pk=emp_id)
        
        
        e=emp()
        e.name=emp_name
        e.email=emp_email
        e.position=emp_position
        e.department=emp_department
        
        
        e.save()
    return redirect("/emp/home/")
    