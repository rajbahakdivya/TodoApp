# Generated by Django 5.0.1 on 2024-01-24 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otptoken',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='OTPToken',
        ),
    ]
