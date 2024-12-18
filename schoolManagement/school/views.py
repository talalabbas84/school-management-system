from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, NewsletterForm, SignupForm
from .models import Course, Teacher, Student

def home(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'index.html', {'courses': courses, 'teachers': teachers})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Thank you for your message!")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            return HttpResponse("You have signed up for the newsletter!")
    else:
        form = NewsletterForm()
    return render(request, 'newsletter.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Signup successful!")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})