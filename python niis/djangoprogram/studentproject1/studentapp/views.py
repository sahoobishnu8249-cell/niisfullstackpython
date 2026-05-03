from django.shortcuts import render
from .models import Student

def student_form(request):
    if request.method == 'POST':
        r = request.POST.get('rollno')
        n = request.POST.get('name')
        m = request.POST.get('mark')

        Student.objects.create(
            rollno=r,
            name=n,
            mark=m
        )

        return render(request, 'success.html')

    return render(request, 'form.html')