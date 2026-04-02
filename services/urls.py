from django.urls import path
from . import views

urlpatterns = [
    path("liste/", views.liste_traiteurs, name="liste_traiteur"),
    path("signup/", views.SignUp, name="signup"),
    path("addtraiteur/", views.addTraiteur, name="addtraiteur"),
    path("", views.accueil, name="accueil"),
    path("traiteur/<int:id>/", views.detail_traiteur, name="detail_traiteur"),
]