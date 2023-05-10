from django.urls import path
from . import views

app_name = 'news_blog'


urlpatterns = [
    path('', views.NewsList.as_view(), name='news_list'),
    path('newsentry/', views.NewsEntry.as_view(), name='news_entry'),\
    path('news/<int:title_id>/', views.NewsDetails.as_view(), name='news_details'),
]
