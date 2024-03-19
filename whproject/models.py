# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class AuditLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(_("ip address"), protocol='both', blank=True, null=True)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        app_label = 'whproject'    
