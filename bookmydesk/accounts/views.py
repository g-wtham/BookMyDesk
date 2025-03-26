from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, template_name='signup.html', context={'form': form})

def home_view(request):
    return render(request, "home.html")