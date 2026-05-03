from django.shortcuts import render, redirect
from .models import Employee

# CREATE
def add_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        salary = request.POST['salary']

        Employee.objects.create(name=name, email=email, salary=salary)
        return redirect('/view/')

    return render(request, 'emp_app/add.html')


# READ
def view_emp(request):
    data = Employee.objects.all()
    return render(request, 'emp_app/view.html', {'emp': data})


# EDIT
def edit_emp(request, id):
    data = Employee.objects.get(id=id)
    return render(request, 'emp_app/update.html', {'emp': data})


# UPDATE
def update_emp(request, id):
    data = Employee.objects.get(id=id)

    data.name = request.POST['name']
    data.email = request.POST['email']
    data.salary = request.POST['salary']
    data.save()

    return redirect('/view/')


# DELETE
def delete_emp(request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect('/view/')