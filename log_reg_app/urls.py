from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_page),
    path('register/', views.regist_user),
    path('login/', views.login_page),
    path('user_login/', views.login_user),
    path('trees/logout/', views.logout),
    
]
