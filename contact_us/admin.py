from django.contrib import admin
from .models import ContactUs


# Register your models here.

@admin.register(ContactUs)
class Subscriber(admin.ModelAdmin):
    list_display = ['email', 'subject', 'name', 'subject', 'description',
                    'date', ]
