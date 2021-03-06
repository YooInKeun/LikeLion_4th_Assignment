"""gameproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import halligalli.views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',halligalli.views.home, name = 'home'),
    path('play_game/',halligalli.views.play_game, name = 'play_game'),
    path('show_card/',halligalli.views.show_card, name = 'show_card'),
    path('confirm/',halligalli.views.confirm, name = 'confirm'),
    path('end_check/',halligalli.views.end_check, name = 'end_check'),
    path('end_check2/',halligalli.views.end_check2, name = 'end_check2'),
    path('register/',halligalli.views.register, name = 'register'),
]
