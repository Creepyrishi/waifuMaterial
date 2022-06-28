"""Anime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # sfw
    path('/sfw/waifu', include('home.urls')),
    path('/sfw/neko', include('home.urls')),
    path('/sfw/shinobu', include('home.urls')),
    path('/sfw/megumin', include('home.urls')),
    path('/sfw/bully', include('home.urls')),
    path('/sfw/cuddle', include('home.urls')),
    path('/sfw/cry', include('home.urls')),
    path('/sfw/hug', include('home.urls')),
    path('/sfw/awoo', include('home.urls')),
    path('/sfw/kiss', include('home.urls')),
    path('/sfw/lick', include('home.urls')),
    path('/sfw/pat', include('home.urls')),
    path('/sfw/smug', include('home.urls')),
    path('/sfw/bonk', include('home.urls')),
    path('/sfw/yeet', include('home.urls')),
    path('/sfw/blush', include('home.urls')),
    path('/sfw/smile', include('home.urls')),
    path('/sfw/wave', include('home.urls')),
    path('/sfw/highfive', include('home.urls')),
    path('/sfw/handhold', include('home.urls')),
    path('/sfw/nom', include('home.urls')),
    path('/sfw/bite', include('home.urls')),
    path('/sfw/glomp', include('home.urls')),
    path('/sfw/slap', include('home.urls')),
    path('/sfw/kill', include('home.urls')),
    path('/sfw/kick', include('home.urls')),
    path('/sfw/happy', include('home.urls')),
    path('/sfw/wink', include('home.urls')),
    path('/sfw/poke', include('home.urls')),
    path('/sfw/dance', include('home.urls')),
    path('/sfw/cringe', include('home.urls')),
    #nsfw
    path('/nsfw/waifu', include('home.urls')),
    path('/nsfw/neko', include('home.urls')),
    path('/nsfw/trap', include('home.urls')),
    path('/nsfw/blowjob', include('home.urls')),
]
