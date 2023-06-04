from django.urls.resolvers import URLPattern
from backend import views

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  
    path('Evenement/', views.EventAPI),
    path('Evenement/<int:pk>/', views.EventAPI),
    path('PI/', views.PIAPI),
    path('PI/<int:pk>/', views.PIAPI),
    path('Commentaire/', views.CommentaireAPI),
    path('Commentaire/<int:pk>/', views.CommentaireAPI),
    path('MoyenTransport/', views.MTAPI),
    path('MoyenTransport/<int:pk>/', views.MTAPI),
    path('Region/', views.RegionAPI),
    path('Region/<int:pk>/', views.RegionAPI),
    path('Visiteur/', views.VisiteurAPI),
]