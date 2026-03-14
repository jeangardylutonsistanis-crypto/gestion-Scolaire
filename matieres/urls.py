from django.urls import path
from . import views

urlpatterns = [
    path('', views.matiere_list, name='matiere_list'),
    path('<int:pk>/', views.matiere_detail, name='matiere_detail'),
    path('creer/', views.matiere_create, name='matiere_create'),
    path('<int:pk>/modifier/', views.matiere_update, name='matiere_update'),
    path('<int:pk>/supprimer/', views.matiere_delete, name='matiere_delete'),
]
