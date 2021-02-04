from django.urls import path
#from accounts import views
from django.contrib.auth import views as authviews
from . import views


app_name= 'accounts'

urlpatterns= [
    #path('login/', views.user_login, name= 'user_login'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.lecturer_register, name= 'register'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
