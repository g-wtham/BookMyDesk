from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import scanHistory
from django.http import JsonResponse

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, template_name="login.html", context= {'login_form': form})

@login_required
def scan_barcode(request):
    barcode = request.GET.get("barcode").strip()
    
    if scanHistory.objects.filter(barcode_data=barcode).exists():
        return JsonResponse({"error" : "Already scanned!"})
    
    scanHistory.objects.create(user=request.user, barcode_data=barcode)
    return JsonResponse({"success": "Saved succesfully!!"})

