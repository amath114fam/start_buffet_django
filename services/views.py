from django.shortcuts import render, get_object_or_404, redirect
from .models import Traiteur
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from .forms import TraiteurForm

# Create your views here.
def liste_traiteurs(request):
    liste_traiteurs = Traiteur.objects.all()
    context = {
        'liste_traiteur' : liste_traiteurs
    }
    return render(request, 'services/liste.html', context)

def accueil(request):
   return render(request, 'services/accueil.html')

def detail_traiteur(request, id):
    traiteur = get_object_or_404(Traiteur, id=id)
    context = {
        'traiteur' : traiteur
    }
    return render(request, 'services/detail.html', context)

def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   
        print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def addTraiteur(request):
    if not request.user.is_authenticated:   
        return redirect('login')            

    if request.method == "POST":
        form = TraiteurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_traiteur')
        print(form.errors)
    else:
        form = TraiteurForm()
    return render(request, 'services/addTraiteur.html', {'form': form})