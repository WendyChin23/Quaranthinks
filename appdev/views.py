from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import(get_object_or_404,render,HttpResponseRedirect)
from .forms import AccountUserForm
from django.core.mail import send_mail, BadHeaderError
from tech import settings  
from django.urls import reverse
from django.contrib import messages


from appdev.models import *
# Create your views here.

class Home(View):
	def get(self, request):
		return render(request,'index.html')

class About(View):
	def get(self, request):
		return render(request,'about.html')

class Blogsingle(View):
	def get(self, request):
		return render(request,'blog-single.html')

class Blog(View):
	def get(self, request):
		return render(request,'blog.html')

class Team(View):
	def get(self, request):
		return render(request,'team.html')

class Contact(View):
	def get(self, request):
		return render(request,'contact.html',{})

	def post(self, request):
		conform = ContactForm(request.POST)
		if request.method == "POST": 
			if conform.is_valid():
				name = request.POST.get("name")
				subject = request.POST.get("subject")
				email = request.POST.get("email")
				message = request.POST.get("message")

				conform = ContactMessage(name = name, subject = subject, email = email, message = message) 
				conform.save()
				send_mail(name,message,email,[settings.EMAIL_HOST_USER], fail_silently = False,)
				return render(request, 'contact.html', {'name': name})
			else:
				print(form.errors)
				pok = "Not send message"
				return HttpResponse(pok)          
		

class GradesView(View):
	def get(self, request):
		grades = Grade.objects.all()

		context = {
			'grades' :grades, #name that we want to use
			
		}
		return render(request,'grades.html',context)

class Members(View):
	def get(self, request):
		return render(request,'members.html')

	def post(self, request):
		if request.method == 'POST':
			username = request.POST.get("username")
			password = request.POST.get("password")
			check_user = AccountUser.objects.filter(username=username, password=password)

			if check_user:		
				return render(request, 'accountuser.html',{'user':check_user})
			else:	
				return HttpResponse('not valid')
		else:	
			return render(request,"signup.html", context)

class Portfolio(View):
	def get(self, request):
		return render(request,'portfolio-details.html')

class Rewards(View):
	def get(self, request):
		return render(request,'rewards.html')

class Services(View):
	def get(self, request):
		return render(request,'services.html')

class Signup(View):
	def get(self, request):
		return render(request,'signup.html')

		
class AdminDashboard(View):
	def get(self, request):
		return render(request,'admindashboard.html')

class AdminPage(View):
	def get(self, request):
		return render(request,'adminpage.html')

class Testimonial(View):
	def get(self, request):
		return render(request,'testimonials.html')

class AccountDashboardView(View):
	def get(self, request):
		accountuser = AccountUser.objects.all()
	   
		context = {
			'accountuser' : accountuser, #name that we want to use
			
		}
		return render(request,'Accountuser.html', context)

	def post(self, request):
		if request.method == 'POST':
			if 'BtnUpdate' in request.POST:
				print('update button clicked')
				Idn = request.POST.get("idn-idn")                                                                                                                                                                                                                                                                                                                                            
				fname = request.POST.get("first_name")
				lname = request.POST.get("last_name")
				Email = request.POST.get("email")             
				Address = request.POST.get("address")
				Age = request.POST.get("age")
				Birthdate = request.POST.get("birthdate")
				Username = request.POST.get("username")
				Password = request.POST.get("password")
				
				update_user = AccountUser.objects.filter(idn=Idn).update(firstname = fname, lastname = lname, address = Address,
				email = Email, age = Age, birthdate = Birthdate, username = Username, password = Password )
				print(update_user)
				print('user updated')

			elif 'BtnDelete' in request.POST:
				print('delete button clicked')
				Idn = request.POST.get("iidn-idn")
				students = AccountUser.objects.filter(idn=Idn).delete()

		return redirect('appdev:accountdashboard_view')


class Signup(View):
	# def get(self, request):
	#     return render(request, 'student.html')

	# def post(self, request):
	#     form = StudentForm(request.POST)
	#     if form.is_valid():
	#         studentid = request.POST.get("course_id")
	#         coursesname = request.POST.get("course_name")

	#         form = Course(course_id = courseid, course_name = coursesname)
	#         form.save()

	#         return redirect('myapp1:dashboard_view')

	#     else:
	#         print(form.errors)
	#         return HttpResponse('not valid')

	def get(self, request):
		return render(request, 'signup.html')

	def post(self, request):        
		form = AccountUserForm(request.POST)        
		# fname = request.POST.get("firstname")
		# print(fname)
		# lname = request.POST.get("lastname")
		# print(lname)
		if form.is_valid():
			# try:
			fname = request.POST.get("first_name")
			lname = request.POST.get("last_name")
			Email = request.POST.get("email")
			Address = request.POST.get("address")
			Age = request.POST.get("age")
			Birthdate = request.POST.get("birthdate")
			Username = request.POST.get("username")
			Password = request.POST.get("password")
			form = AccountUser(first_name = fname, last_name = lname, email = Email, address = Address, age = Age,
			 birthdate = Birthdate, username = Username, password=Password)
			print('clicked')
			form.save() 

			#return HttpResponse('Student record saved!')           
			return redirect('appdev:members_view')
			# except:
			#   raise Http404
		else:
			print(form.errors)
			return HttpResponse('not valid')	
	#def post(self, request):

		# if request.method == "POST":	
		# 	if 'btnRegister' in request.POST:
		# 		Uform = AccountUserForm(request.POST)			
		# 		if Uform.is_valid():
		# 			print('clicked')
		# 			user = Uform.save()

		# 			user.refresh_from_db()
		# 			# print('clicked')
		# 			# fname = user.profile.first_name = request.POST.get("first_name")
		# 			# lname = user.profile.last_name = request.POST.get("last_name")
		# 			# email = user.profile.email = request.POST.get("email")
		# 			# address = user.profile.address = request.POST.get("address")
		# 			# age = user.profile.age = request.POST.get("age")
		# 			# bdate = user.profile.birthdate = request.POST.get("birthdate")
		# 			# user.save()			
		# 			# username = request.POST.get("username")
		# 			# password = request.POST.get("password1")

		# 			# form = AccountUser(first_name = fname, last_name = lname, email = email, address = address, age = age,
		# 			# birthdate = bdate)
		# 			# form.save()

		# 			return HttpResponse('Student record saved!')
		# 			return redirect('appdev:members_view')
		# 		else:	
		# 			return HttpResponse('not valid')
		# # 			form = AccountUserForm()
		# # context = {'form':form}	

		# # return render(request,"signup.html", context)
				
	

		