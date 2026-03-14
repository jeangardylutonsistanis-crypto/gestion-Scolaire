 

# Vue pour afficher la liste des classes



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Classe
from .forms import ClasseForm
from django.http import HttpResponseForbidden


def is_admin (user):
    return user.is_autenticated and user.is_staff

@login_required
def liste_classes(request):
    classes = Classe.objects.all()
    return render(request, 'classes/liste_classes.html', {'classes': classes})


@login_required
def detail_classe(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    return render(request, 'classes/detail_classe.html', {'classe': classe})


@login_required
def creer_classe(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_classes')
    else:
        form = ClasseForm()
    return render(request, 'classes/creer_classe.html', {'form': form})


@login_required
def modifier_classe(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('liste_classes')
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'classes/modifier_classe.html', {'form': form})


@login_required
def supprimer_classe(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        classe.delete()
        return redirect('liste_classes')
    return render(request, 'classes/supprimer_classe.html', {'classe': classe})
