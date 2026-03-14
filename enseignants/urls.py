from django.urls import path
from . import views

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.enseignant_list, name='enseignant_list'),
    path('<int:pk>/', views.enseignant_detail, name='enseignant_detail'),
    path('create/', views.enseignant_create, name='enseignant_create'),
    path('<int:pk>/edit/', views.enseignant_update, name='enseignant_update'),
    path('<int:pk>/delete/', views.enseignant_delete, name='enseignant_delete'),
]
