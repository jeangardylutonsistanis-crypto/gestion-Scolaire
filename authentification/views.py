from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, LoginForm
from django.contrib import messages

def base (request):
    return render(request, 'base.html')

def home (request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Compte créé avec succès.")
            return redirect('/')  # Ranplase ak paj prensipal ou
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie.")
            return redirect('/')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def logout_view(request):
    logout(request)
    request.session.flush()  # retire tout done nan sesyon an
    messages.info(request, "Déconnecté avec succès.")
    return redirect('home')  # redirije sou paj ak navbar



@login_required
def logout_confirm_view(request):
    return render(request, 'logout_confirm.html')
