from django.contrib import admin
from .models import IiotUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(IiotUser,UserAdmin)

# Register your models here.
