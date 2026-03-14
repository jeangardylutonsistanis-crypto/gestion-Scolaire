from django.shortcuts import render, get_object_or_404, redirect
from .models import Cours
from .forms import CoursForm
from django.http import HttpResponseForbidden
 

# Liste tous les cours
def cours_list(request):
    cours = Cours.objects.all()
    return render(request, 'cours_list.html', {'cours': cours})

# Ajouter un nouveau cours
def cours_create(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cours_list')
    else:
        form = CoursForm()
    return render(request, 'cours_form.html', {'form': form})

# Modifier un cours
def cours_update(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)
        if form.is_valid():
            form.save()
            return redirect('cours_list')
    else:
        form = CoursForm(instance=cours)
    return render(request, 'cours_form.html', {'form': form})

# Supprimer un cours
def cours_delete(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        cours.delete()
        return redirect('cours_list')
    return render(request, 'cours_confirm_delete.html', {'cours': cours})
