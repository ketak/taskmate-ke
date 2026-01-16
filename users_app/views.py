from django.shortcuts import redirect, render
from .forms import CustomUserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        register_form = CustomUserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "User registered successfully. Login to continue.")
            return redirect("register")
    else:   
        
        register_form = CustomUserRegisterForm()
    return render(request, "register.html", {"register_form": register_form})