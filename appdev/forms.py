from django import forms
#from django.db.models import fields
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields= '__all__'

class AccountUserForm(forms.ModelForm):
    class Meta:
        model = AccountUser
     
        fields= '__all__'

    
