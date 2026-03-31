from django.urls import path,include
from .views import upload, file_list
from django.contrib import admin

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('list/', file_list, name='file_list'),
]
