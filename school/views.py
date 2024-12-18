from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Teacher, Student

def home(request):
    return render(request, 'index.html')

def display_data(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    return render(request, 'index.html', {
        'courses': courses,
        'teachers': teachers,
        'students': students
    })

def contact_form(request):
    if request.method == 'POST':
        return HttpResponse("Contact form received successfully!")
    return render(request, 'index.html')
