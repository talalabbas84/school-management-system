from django import forms
from .models import Student, Teacher

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class NewsletterForm(forms.Form):
    email = forms.EmailField()

class SignupForm(forms.ModelForm):
    CHOICES = [('Student', 'Student'), ('Teacher', 'Teacher')]
    user_type = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'student_id']