from django import forms
# from borrow.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True, help_text='First name')
#     last_name = forms.CharField(max_length=30, required=True, help_text='Last name')
#     gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'),('O', 'Other')], required=True)
#     age = forms.IntegerField(required=True)
#     student_id = forms.CharField(max_length=15, required=True)
#     faculty = forms.CharField(max_length=50, required=True)
#     email = forms.EmailField(required=True)
#     phone_number = forms.CharField(max_length=15, required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'gender', 'age', 'student_id', 'faculty', 'email', 'phone_number', 'password1', 'password2')