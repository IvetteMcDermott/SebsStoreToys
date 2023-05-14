from django.urls import path
from . import views

app_name = 'bookmarks'


urlpatterns = [
       path('toggle_bookmark/<int:ware_id>', views.toggle_bookmark, name='toggle_bookmark'),
]
