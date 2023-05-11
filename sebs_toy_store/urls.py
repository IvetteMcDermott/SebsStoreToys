"""sebs_toy_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import handler404, handler500, handler403, handler405


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls'), name='homeapp_urls'),
    path('store/', include('sts_store.urls'), name='sts_store'),
    path('profiles/', include('profiles.urls'), name='profiles'),
    path('shoppingcart/', include('shopping_cart.urls'), name='shopping_cart'),
    path('checkout/', include('checkout.urls'), name='checkout'),
    path('newsletter/', include('mailchimpNewsletter.urls'), name='subscribeToNewsLetter'),
    path('bookmarks/', include('bookmarks.urls'), name='bookmarks'),
    path('news_blog/', include('news_blog.urls'), name='news_blog'),
    path('reviews/', include('reviews.urls'), name='reviews'),
    path('contact_us/', include('contact_us.urls'), name='contact_us'),
]

handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'
handler403 = 'home.views.handler403'
handler405 = 'home.views.handler405'