from django.urls import path

from accounts import views
from accounts.views import logout_

app_name = 'accounts'
urlpatterns = [
    path('google/',views.google_login,name='google_login'),
    path('register/', views.register, name='register'),
    path('login/', views.login_, name='login'),
    path('logout/', logout_, name='logout'),
]
