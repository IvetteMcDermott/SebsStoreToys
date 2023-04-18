from django.urls import path
from . import views

app_name = 'shopping_cart'


urlpatterns = [
        path('', views.view_cart, name='view_cart'),
        path('add/<ware_id>/', views.add_to_cart, name='add_to_cart'),
        path('modify/<ware_id>/', views.modify_cart, name='modify_cart'),
        path('remove/<ware_id>/', views.remove_from_cart, name='remove_from_cart'),
    ]
