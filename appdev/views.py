from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import(get_object_or_404,render,HttpResponseRedirect)
from .forms import *
from appdev.forms import AccountUserForm

from appdev.models import AccountUser
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
		return render(request,'contact.html')

class Grades(View):
	def get(self, request):
		return render(request,'grades.html')

class Members(View):
	def get(self, request):
		return render(request,'members.html')

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
                fname = request.POST.get("first-name")
                lname = request.POST.get("last-name")
                Email = request.POST.get("email-email")				
                Address = request.POST.get("address-address")
                Age = request.POST.get("age-age")
                Birthdate = request.POST.get("birth-date")
                Username = request.POST.get("user-name")
                Password = request.POST.get("pass-word")
				
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
            
			Idn = request.POST.get("idn")
			fname = request.POST.get("firstname")
			lname = request.POST.get("lastname")
			Address = request.POST.get("address")
			Age = request.POST.get("age")
			Birthdate = request.POST.get("birthdate")
			Username = request.POST.get("username")
			Password = request.POST.get("password")
			form = AccountUser(idn = Idn, firstname = fname, lastname = lname, address = Address, age = Age,
			 birthdate = Birthdate, username = Username, password=Password)
			form.save()	

			#return HttpResponse('Student record saved!')			
			return redirect('appdev:members_view')
			# except:
			# 	raise Http404
		else:
			print(form.errors)
			return HttpResponse('not valid')
		