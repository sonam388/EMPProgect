from django.shortcuts import render , redirect
from .models import Employee

# Create your views here.

# View All Employee
def employee_list(request):
    employees = Employee.objects.all()
    return render (request , 'employees/employees_list.html' , {'employee':employees})


# Add All Employees

def addEmployees(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            department=request.POST['department'],
            salary=request.POST['salary']
        )
        return redirect("employee_list")
    return render(request , "employees/add_employees.html")