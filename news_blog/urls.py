from django.urls import path
from . import views

app_name = 'news_blog'


urlpatterns = [
    path('', views.NewsList.as_view(), name='news_list'),
    path('addnews/', views.NewsEntry.as_view(), name='add_news'),
    path('news/<int:title_id>/', views.NewsDetails.as_view(),
         name='news_details'),
    path('<int:title_id>/newsedit/', views.news_edit, name='news_edit'),
    path('<int:title_id>/newsdelete/', views.news_delete, name='news_delete'),
]
