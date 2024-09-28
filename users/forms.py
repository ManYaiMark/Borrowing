from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], required=True)
    age = forms.IntegerField(required=True)
    student_id = forms.CharField(max_length=15, required=True)
    faculty = forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'gender', 'age', 'student_id', 'faculty', 'phone_number', 'password1', 'password2')

# class FormLogin(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['student_id','email','password1']
#     label = {
#         'student_id' : 'รหัสนักศึกษา',
#         'email' : 'อีเมล',
#         'password1' : 'รหัสผ่าน',
#     }