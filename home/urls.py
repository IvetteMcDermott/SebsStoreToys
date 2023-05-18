from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='home'),
    path('q&a/', views.q_a, name='q_a'),
    path('terms/', views.terms, name='terms'),
]
