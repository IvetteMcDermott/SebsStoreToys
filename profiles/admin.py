from django.contrib import admin
from .models import UserProfile


# Register your models here.

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['filter_name', 'filter_name',]
    list_filter = ('user_name',)
    search_fields = ['user_name', ]
