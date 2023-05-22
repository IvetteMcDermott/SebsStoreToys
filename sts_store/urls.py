from django.urls import path
from . import views

app_name = 'sts_store'


urlpatterns = [
    path('store/', views.Store.as_view(), name='wares'),
    path('ware/<int:ware_id>/', views.WareDetail.as_view(),
         name='ware_detail'),
    path('reply/<int:review_id>/', views.reply_review, name='reply_review'),
    path('<int:ware_id>/wareedit/', views.WareEdit, name='ware_edit'),
    path('<int:ware_id>/waredelete/', views.WareDelete, name='ware_delete'),
    path('image/<int:image_id>/', views.open_image, name='open_image'),
    path('<int:id>/imagedelete/', views.image_delete, name='image_delete'),
    path('staffpanel/', views.StaffPanel, name='staff_panel'),
    path('search/', views.search, name='search'),
    path('search_category/', views.search_category, name='search_category'),
    path('wareentry/', views.WareEntry.as_view(), name='ware_entry'),
    path('imageentry/', views.AddImageForm.as_view(), name='image_entry'),
    path('orders/', views.orders_list, name='orders'),
    path('contacted_us/', views.contacted_us_list, name='contacted_us'),
]
