from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_classes, name='liste_classes'),
    path('<int:pk>/', views.detail_classe, name='detail_classe'),
    path('creer/', views.creer_classe, name='creer_classe'),
    path('<int:pk>/modifier/', views.modifier_classe, name='modifier_classe'),
    path('<int:pk>/supprimer/', views.supprimer_classe, name='supprimer_classe'),
]
