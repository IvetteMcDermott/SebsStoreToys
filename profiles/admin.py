from django.contrib import admin
from .models import UserProfile


# Register your models here.

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('user',)}
    list_display = ['user', 'first_name', 'last_name',]
    search_fields = ['user', ]
