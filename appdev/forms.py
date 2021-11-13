from django import forms
#from django.db.models import fields
from .models import *

class AccountUserForm(forms.ModelForm):
    class Meta:
        model = AccountUser
     
        fields= '__all__'

        

    
