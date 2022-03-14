from django.shortcuts import render, redirect
from .forms import *

def home_view(request):
    if request.method == 'POST':
        contactForm = ContactForm(request.POST)
        registerForm = RegisterForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            return redirect('/')
        if registerForm.is_valid():
            registerForm.save()
            return redirect('/')
    else:
        contactForm = ContactForm(request.POST)
        registerForm = RegisterForm(request.POST)

    context = {
        'contactForm': contactForm,
        'registerForm': registerForm,
    }

    return render(request, 'index.html', context)
