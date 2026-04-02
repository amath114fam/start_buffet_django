# 🍽️ Star Buffet — Plateforme de Gestion des Traiteurs

Star Buffet est une plateforme de mise en relation pour les événements (mariages, baptêmes, réceptions). Ce module gère les traiteurs : affichage, détail, ajout et authentification.

---

## 📋 Étapes de Développement

### Étape 1 — Architecture & Modélisation
- Création du projet `starbuffet_project` et de l'application `services`
- Définition du modèle `Traiteur` dans `models.py`
- Application des migrations (`makemigrations` + `migrate`)
- Enregistrement du modèle dans `admin.py`

### Étape 2 — Affichage de la liste (`/traiteurs/`)
- Vue `liste_traiteur` avec `Traiteur.objects.all()`
- Template `liste.html` avec cards (Nom, Spécialité, bouton "Voir le profil")

### Étape 3 — Détail dynamique (`/traiteurs/<int:id>/detail/`)
- Route avec paramètre `<int:id>`
- Récupération avec `get_object_or_404`
- Affichage complet (description, contact, adresse)

### Étape 4 — Authentification & Sécurité
- Système d'auth natif Django (`django.contrib.auth.urls`)
- Pages Connexion et Déconnexion personnalisées
- Protection de l'ajout avec `@login_required` ou 
- Protection de l'ajout avec if not request.user.is_authenticated (que j'ai utilisé)  

### Étape 5 — Ajout de Contenu (ModelForm)
- `TraiteurForm` basé sur `ModelForm`
- Page `/addtraiteur/` avec formulaire complet
- Gestion de l'upload d'image (`request.FILES` + `enctype="multipart/form-data"`)

---
