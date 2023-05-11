from django.urls import path
from . import views

app_name = 'contact_us'


urlpatterns = [
       path('', views.contact_us, name='contact_us_form'),
       path("success/", views.success, name="success"),
       path("error/", views.error, name="error"),
]
