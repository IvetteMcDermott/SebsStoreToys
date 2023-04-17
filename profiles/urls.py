from django.urls import path
from . import views

app_name = 'profiles'


urlpatterns = [
       path('my_profile/', views.my_profile, name='my_profile'),
]
