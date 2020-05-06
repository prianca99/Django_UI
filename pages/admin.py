from django.contrib import admin

# Register your models here.
from .models import UserRequests

admin.site.register(UserRequests)
