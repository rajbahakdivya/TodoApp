from django import forms 
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class TaskForm (forms.ModelForm):
     title = forms.CharField(widget=forms.TextInput(attrs={"class":"todo-container", "placeholder":"Enter Todo"}))
     class Meta:
      model = Task
      fields = ["title"]

class RegisterForm(UserCreationForm):
   email= forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Enter email-address", "class": "form-control"} ))
   username= forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Enter email-username", "class":"form-control"}))
   password1= forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder":"Enter password", "class": "form-control"}))
   password1= forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder":"Confirm password", "class": "form-control"}))
   
   class Meta:
      model = get_user_model()
      fields = ["email", "username", "password1", "password2"]

      
