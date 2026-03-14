from django.urls import path
from . import views

urlpatterns = [
    path('', views.cours_list, name='cours_list'),
    path('create/', views.cours_create, name='cours_create'),
    path('update/<int:pk>/', views.cours_update, name='cours_update'),
    path('delete/<int:pk>/', views.cours_delete, name='cours_delete'),
]
