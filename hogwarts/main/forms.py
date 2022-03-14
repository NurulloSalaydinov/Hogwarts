from django import forms
from .models import Contact, Register

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'