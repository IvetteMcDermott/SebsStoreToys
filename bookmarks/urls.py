from django.urls import path
from . import views

app_name = 'bookmarks'


urlpatterns = [
       path('', views.bookmarks, name='my_bookmarks'),
       path('toggle_bookmark/<int:ware_id>', views.toggle_bookmark, name='toggle_bookmark'),
]
