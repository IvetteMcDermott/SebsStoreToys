from django.urls import path
from . import views


urlpatterns = [
    path('store', views.Store.as_view(), name='wares'),
    path('ware/<int:ware_id>', views.WareDetail.as_view(), name='ware_detail'),
]