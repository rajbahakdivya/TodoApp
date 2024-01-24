
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from  django.conf import settings
import secrets

# For todo
class Task(models.Model):
    title= models. CharField(max_length=200)
    completed = models. BooleanField(default=False)
    created_at = models. DateTimeField(auto_now_add=True)
    updated_at = models. DateTimeField(auto_now=True)

def __str__(self):
    return self.title 


# for login

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # def __str__(self):
    #     return self.email
    

# for otp 
    
class OTPToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name="otps")
    otp_code = models.CharField(max_length=6, default=secrets.token_hex(3))
    tp_created_at = models.DateTimeField(auto_now_add=True)
    otp_expires_at = models.DateTimeField(blank=True, null=True)

def __str__ (self):

    
    return self.user.username
