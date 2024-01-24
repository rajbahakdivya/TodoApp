from django.contrib import admin
from .models import Task
from .models import CustomUser, OTPToken
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry

admin.site.register(LogEntry)
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )


class OtpTokenAdmin(admin.ModelAdmin):
    list_display = ("user", "otp_code")


admin.site.register(OTPToken, OtpTokenAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

# todo app

admin.site.register(Task)