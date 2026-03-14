from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/confirm/', views.logout_confirm_view, name='logout_confirm'),

    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
]
