from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Etudiant
from .forms import EtudiantForm
from .models import Absence
from .forms import AbsenceForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def test_view(request):
    return HttpResponse(f"Ou konekte kòm {request.user.username}, staff: {request.user.is_staff}")




def is_admin(user):
    return user.is_authenticated and user.is_staff
    


def etudiant_list(request):
    etudiants = Etudiant.objects.all().order_by('nom')  # Triye pa nom (pi bèl vizyèlman)

    # Pagination: 10 elèv pa paj
    paginator = Paginator(etudiants, 10)
    page = request.GET.get('page')

    try:
        etudiants_page = paginator.page(page)
    except PageNotAnInteger:
        etudiants_page = paginator.page(1)
    except EmptyPage:
        etudiants_page = paginator.page(paginator.num_pages)

    return render(request, 'etudiants/etudiant_list.html', {
        'etudiants': etudiants_page,
        'paginator': paginator,
        'page_obj': etudiants_page,  # pou compatibilite ak tag Django
    })
def etudiant_detail(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    return render(request, 'etudiants/etudiant_detail.html', {'etudiant': etudiant})
@login_required
def etudiant_create(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
    
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etudiant_list')
    else:
        form = EtudiantForm()
    return render(request, 'etudiants/etudiant_form.html', {'form': form})
@user_passes_test(is_admin)
def etudiant_update(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiant_detail', pk=etudiant.pk)
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'etudiants/etudiant_form.html', {'form': form})
@user_passes_test(is_admin)
def etudiant_delete(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('etudiant_list')
    return render(request, 'etudiants/etudiant_confirm_delete.html', {'etudiant': etudiant})





class AbsenceListView(ListView):
    model = Absence
    template_name = 'etudiants/absence_list.html'
    context_object_name = 'absences'

from django.shortcuts import redirect
from django.contrib import messages

class AbsenceCreateView(CreateView):
    model = Absence
    form_class = AbsenceForm
    template_name = 'etudiants/absence_form.html'
    success_url = '/etudiants/absences/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            messages.error(request, "Ou pa gen dwa ajoute absans.")
            return redirect('absence_list')
        return super().dispatch(request, *args, **kwargs)
