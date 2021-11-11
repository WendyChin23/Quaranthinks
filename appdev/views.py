from django.shortcuts import render
from django.views.generic import View
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
