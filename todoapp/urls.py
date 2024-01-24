from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("register", views.signup, name="register"),
    path("verify-email/<slug:username>", views.verify_email, name="verify-email"),
    path("resend-otp", views.resend_otp, name="resend-otp"),
    path("login", views.signin, name="signin"),
    path("task", views.task_list, name="task-list"),
    path("task/<int:pk>/update", views.task_update, name="task-update"),
    path("task/<int:pk>/delete", views.task_delete, name="task-delete")
    
]