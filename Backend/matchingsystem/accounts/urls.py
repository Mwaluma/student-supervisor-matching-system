from django.urls import path, re_path
from django.contrib.auth import views as authviews
from . import views
from django.conf.urls import url, include


app_name= 'accounts'

urlpatterns= [
    #path('login/', views.user_login, name= 'user_login'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.lecturer_register, name= 'register'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update/<str:pk>/', views.update_profile, name='update_profile'),
    path('delete/<str:pk>/', views.delete_something, name='delete'),
    path('', views.home, name='home'),
    path('match/', views.find_match, name='find_match'),
    path('results/', views.results, name='results'),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/', authviews.PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', authviews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset-password/confirm/<uidb64>/<token>/', authviews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    # authviews.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', authviews.PasswordResetConfirmView.as_view(),
    #         name='password_reset_confirm'),
]
