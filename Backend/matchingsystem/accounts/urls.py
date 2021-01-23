from django.urls import path
#from accounts import views
from django.contrib.auth import views as authviews
from . import views


app_name= 'accounts'

urlpatterns= [
    #path('login/', views.user_login, name= 'user_login'),
    path('login/', authviews.LoginView.as_view(), name='login'),
    path('logout/', authviews.LogoutView.as_view(next_page= '/'), name='logout'),
    path('register/', views.lecturer_register, name= 'register'),
]
