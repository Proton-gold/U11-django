"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from Book.views import home, list_1, list_create, delete_list, list_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('list/', list_1, name='list'),
    path('create/', list_create, name='create'),
    path('delete/<int:pk>', delete_list, name='delete'),
    path('update/<int:pk>',list_update, name='update'),


]
