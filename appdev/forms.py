from django import forms
#from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactMessage
		fields= '__all__'

class AccountUserForm(forms.ModelForm):
	class Meta:
		model = AccountUser
		fields= ['email' , 'username']
		#fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2', 'address', 'age', 'birthdate')

	# class clean_email(self):
	# 	email = self.cleaned_data['email'].lower()
	# 	r = AccountUser.objects.filter(email=email)
	# 	if r.count():
	# 		raise  ValidationError("Email already exists")
	# 		return email  

	# class clean_username(self):
	# 	username = self.cleaned_data['username'].lower()
	# 	s = AccountUser.objects.filter(username=username)
	# 	if s.count():
	# 		raise  ValidationError("Username already exists")
	# 		return username   

class GradeForm(forms.ModelForm):
	class Meta:
		model = Grade 
		fields= '__all__'      

class DonationForm(forms.ModelForm):
	class Meta:
		model = Donation 
		fields= '__all__'  		 

	
