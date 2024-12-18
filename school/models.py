from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    enrollment_capacity = models.IntegerField()
    semesters = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    staff_id = models.CharField(max_length=10, unique=True, primary_key=True)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=10, unique=True)
    enrollment_date = models.DateField()
    registered_courses = models.ManyToManyField(Course)
