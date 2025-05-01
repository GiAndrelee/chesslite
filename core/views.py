
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
import random

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'core/profile.html')

def get_tip(request):
    tips = [
        "Control the center of the board.",
        "Develop your knights before your bishops.",
        "Don’t move the same piece twice in the opening.",
        "Castle early to protect your king.",
        "Watch for hanging pieces.",
        "Use all your pieces — don’t leave them stuck.",
        "Think one move ahead at all times.",
    ]
    return JsonResponse({'tip': random.choice(tips)})

def logout_view(request):
    logout(request)
    return redirect('register')  # or change to 'home' if you want to go to homepage
