from django.urls import path
from post import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:id>/comment/', views.add_comment, name='add_comment')
]