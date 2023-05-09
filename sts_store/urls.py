from django.urls import path
from . import views

app_name = 'sts_store'


urlpatterns = [
    path('store/', views.Store.as_view(), name='wares'),
    path('ware/<int:ware_id>/', views.WareDetail.as_view(), name='ware_detail'),
    path('<int:ware_id>/wareedit/', views.WareEdit, name='ware_edit'),
    path('<int:ware_id>/waredelete/', views.WareDelete, name='ware_delete'),
    path('<int:image_id>/imagedelete/', views.image_delete, name='image_delete'),
    path('storepanel/', views.StorePanel, name='store_panel'),
    path('search/', views.search, name='search'),
    path('wareentry/', views.WareEntry.as_view(), name='ware_entry'),
    path('imageentry/', views.AddImageForm.as_view(), name='image_entry'),
    path('orders/', views.orders_list, name='orders'),
]
