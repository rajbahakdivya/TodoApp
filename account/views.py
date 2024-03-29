from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponse
from .models import OTPToken
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from todoapp.views import task_list
from .models import CustomUser
import hashlib
from django.contrib.auth.hashers import check_password

# Create your views here.

# This is for signup view


def index(request):
    return render(request, "index.html")


def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! An OTP was sent to your Email")
            return redirect("verify-email", username=request.POST['username'])
        
        
    context = {"form": form}
    return render(request, "signup.html", context)

# This is for email verification

def verify_email(request, username):
    user = get_user_model().objects.get(username=username)
    user_otp = OTPToken.objects.filter(user=user).last()

    if request.method == 'POST':

        #for token validation
        if user_otp.otp_code == request.POST['otp_code']:
           

        # checking if token is expired or not  
            if user_otp.otp_expires_at >timezone.now():
                user.is_activate=True
                user.save()
                messages.success(request, "Account activated successfully!! You can now Login.")
                return redirect("signin")
        # for expired token
            else: 
                messages.warning(request, "The OTP has expired, get a new OtP!")
                return redirect("verify-email",username= user.username)
        
#for invalid otp code
        else:
            messages.warning(request, "Invalid OTP entered, enter a valid OTP!")
            return redirect("verify-email",username= user.username)


    context = {} 
    return render( request, "verify_token.html", context)


# For resend otp
def resend_otp(request):
  if request.method == "POST":
     user_email = request.POST["otp_email"]

     if get_user_model().objects.filter(email=user_email).exists():
         user = get_user_model().objects.get(email=user_email)
         otp = OTPToken.objects.create(user=user, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
                   
        # for email variables
         subject="Email Verification"
         message= f"""
                       Hi {user.username}, here is your OTP {otp.otp_code}
                       It expiresin 5 minute, use the url below to redirect back to the website
                       http://127.0.0.1:8000/verify-email/{user.username} 
                       """
         sender = "divyarajbahak@gmail.com"
         receiver = [user.email,]
 
         # To send mail
         send_mail(
             subject,
             message,
             sender,
             receiver,

         )            
    
         messages.success(request, "A new OTP has been sent to your email-address")
         return redirect("verify-email", username=user.username)
  
     else:
            messages.warning(request, "This email doesn't exixt in the database")
            return redirect("resend-otp")    
  context = {}
  return render(request,"resend_otp.html", context)

def signin(request):
    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']
        user = CustomUser.objects.filter(email=email).first()
      
        if user is not None:
            if check_password(password, user.password):
                            login(request,user)
                            messages.success(request, f"Hi {request.user.username}, you are now logged in")
                            return redirect(task_list)
        else:
            messages.warning(request, "Invalid credentials")
            return redirect("register")
        
    return render(request,"login.html")