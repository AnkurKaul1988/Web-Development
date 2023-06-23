from django.urls import path
from LoginSystemApp import views

app_name = 'LoginSystemApp'

urlpatterns = [
    path('', views.index,name='index' ),
    path('register/', views.register,name='register' ),
    path('login/', views.user_login,name='login' ),
    
]
