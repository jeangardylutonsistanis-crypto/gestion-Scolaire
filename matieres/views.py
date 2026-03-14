from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Matiere
from .forms import MatiereForm
from django.http import HttpResponseForbidden


@login_required
def matiere_list(request):
    matieres = Matiere.objects.all()
    return render(request, 'matieres/matiere_list.html', {'matieres': matieres})


@login_required
def matiere_detail(request, pk):
    matiere = get_object_or_404(Matiere, pk=pk)
    return render(request, 'matieres/matiere_detail.html', {'matiere': matiere})


@login_required
def matiere_create(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    if request.method == 'POST':
        form = MatiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matiere_list')
    else:
        form = MatiereForm()
    return render(request, 'matieres/matiere_form.html', {'form': form})


@login_required
def matiere_update(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    matiere = get_object_or_404(Matiere, pk=pk)
    if request.method == 'POST':
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('matiere_list')
    else:
        form = MatiereForm(instance=matiere)
    return render(request, 'matieres/matiere_form.html', {'form': form})


@login_required
def matiere_delete(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    matiere = get_object_or_404(Matiere, pk=pk)
    if request.method == 'POST':
        matiere.delete()
        return redirect('matiere_list')
    return render(request, 'matieres/matiere_confirm_delete.html', {'matiere': matiere})
