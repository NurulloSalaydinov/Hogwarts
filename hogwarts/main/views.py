from django.shortcuts import render, redirect
from .forms import *
from telepot import Bot

bot = Bot('Your Bot Token')

def home_view(request):
    if request.method == 'POST':
        contactForm = ContactForm(request.POST)
        registerForm = RegisterForm(request.POST)
        if contactForm.is_valid():
            name = request.POST.get('full_name')
            email = request.POST.get('email')
            msg = request.POST.get('message')
            bot.sendMessage('Your Id', f'Hey New Contact\n{name}\n{email}\n{msg}')
            contactForm.save()
            return redirect('/')
        if registerForm.is_valid():
            name = request.POST.get('full_name')
            phone = request.POST.get('phone')
            degree = request.POST.get('degree')
            bot.sendMessage('Your Id', f'Hey New Student\n{name}\n{phone}\n{degree}')
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
