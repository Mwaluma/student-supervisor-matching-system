from django.urls import path
#from accounts import views
from django.contrib.auth import views

app_name= 'accounts'

urlpatterns= [
    #path('login/', views.user_login, name= 'user_login'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page= '/'), name='logout')
]
