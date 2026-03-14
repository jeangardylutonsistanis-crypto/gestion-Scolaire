from django.shortcuts import render, get_object_or_404, redirect
from .models import Enseignant
from .forms import EnseignantForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def is_admin (user):
     return user.is_authenticated and user.is_staff

def base(request):
    return render(request, 'base.html')

# Afficher la liste des enseignants
def enseignant_list(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'enseignants/enseignant_list.html', {'enseignants': enseignants})

# Afficher les détails d'un enseignant

def enseignant_detail(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    return render(request, 'enseignants/enseignant_detail.html', {'enseignant': enseignant})

# Ajouter un nouvel enseignant
@login_required
def enseignant_create(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    if request.method == "POST":
        form = EnseignantForm(request.POST)
        if form.is_valid():
            enseignant = form.save(commit=False)  # pa sove ManyToMany field la toutbon
            enseignant.save()  # sove objè a premye
            form.save_m2m()   # sove ManyToMany (specialite)
            return redirect('enseignant_list')
    else:
        form = EnseignantForm()
    return render(request, 'enseignants/enseignant_form.html', {'form': form})


# Modifier un enseignant existant
@login_required
def enseignant_update(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    enseignant = get_object_or_404(Enseignant, pk=pk)
    if request.method == "POST":
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('enseignant_detail', pk=pk)
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'enseignants/enseignant_form.html', {'form': form})

# Supprimer un enseignant
@login_required
def enseignant_delete(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    enseignant = get_object_or_404(Enseignant, pk=pk)
    if request.method == "POST":
        enseignant.delete()
        return redirect('enseignant_list')
    return render(request, 'enseignants/enseignant_confirm_delete.html', {'enseignant': enseignant})
