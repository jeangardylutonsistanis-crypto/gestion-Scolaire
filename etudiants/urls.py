from django.urls import path
from . import views
from django.urls import path
from .views import AbsenceListView, AbsenceCreateView


urlpatterns = [
    path('etudiant_list', views.etudiant_list, name='etudiant_list'),
    path('etudiant/<int:pk>/', views.etudiant_detail, name='etudiant_detail'),
    path('create', views.etudiant_create, name='etudiant_create'),
    path('etudiant/<int:pk>/edit/', views.etudiant_update, name='etudiant_update'),
    path('etudiant/<int:pk>/delete/', views.etudiant_delete, name='etudiant_delete'),
    path('absences/', AbsenceListView.as_view(), name='absence_list'),
    path('absences/create/', AbsenceCreateView.as_view(), name='absence_create'),
    path('test/', views.test_view, name='test'),

    # incluez d'autres routes si nécessaire
]


