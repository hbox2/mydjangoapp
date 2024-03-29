"""mydjangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from mydjangoapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index.html',views.index, name='index'),
    path('about_us.html',views.about_us, name='about_us'),
    path('contact_us.html',views.contact_us, name='contact_us'),
    path('thank_you.html',views.thank_you, name='thank_you'),
    path('check.html',views.check, name='check'),
    path('admin/', admin.site.urls),
]
