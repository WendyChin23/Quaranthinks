from . import views
from django.urls import path

app_name = 'appdev'

urlpatterns= [
	path('about', views.About.as_view(), name="about_view"),
	path('blogsingle', views.Blogsingle.as_view(), name="blogsingle_view"),
	path('blog', views.Blog.as_view(), name="blog_view"),
	path('', views.Home.as_view(), name="Home_view"),
	path('team', views.Team.as_view(), name="team_view"),
	path('contact', views.Contact.as_view(), name="contact_view"),
	path('grades', views.Grades.as_view(), name="grades_view"),
	path('members', views.Members.as_view(), name="members_view"),
	path('portfolio', views.Portfolio.as_view(), name="portfolio_view"),
	path('rewards', views.Rewards.as_view(), name="rewards_view"),
	path('services', views.Services.as_view(), name="services_view"),
	path('signup', views.Signup.as_view(), name="signup_view"),
	path('testimonial', views.Testimonial.as_view(), name="testimonial_view"),
	path('accountuser', views.AccountDashboardView.as_view(), name="accountdashboard_view"),

]