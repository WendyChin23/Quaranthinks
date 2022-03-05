from django.urls import path
from . import views

app_name = 'appdev'

urlpatterns= [
	path('about', views.About.as_view(), name="about_view"),
	path('blogsingle', views.Blogsingle.as_view(), name="blogsingle_view"),
	path('blog', views.Blog.as_view(), name="blog_view"),
	path('', views.Home.as_view(), name="Home_view"),
	path('team', views.Team.as_view(), name="team_view"),
	path('contact', views.Contact.as_view(), name="contact_view"),
	path('grades', views.GradesView.as_view(), name="grades_view"),
	path('nogrades', views.NoGrade.as_view(), name="nogrades_view"),
	path('members', views.Members.as_view(), name="members_view"),
	path('portfolio', views.Portfolio.as_view(), name="portfolio_view"),
	path('rewards', views.Rewards.as_view(), name="rewards_view"),
	path('services', views.Services.as_view(), name="services_view"),
	path('signup', views.Signup.as_view(), name="signup_view"),
	path('testimonial', views.Testimonial.as_view(), name="testimonial_view"),
	path('accountuser', views.AccountDashboardView.as_view(), name="accountdashboard_view"),
	path('adminpage', views.AdminPage.as_view(), name="admin_view"),
	path('admindashboard', views.AdminDashboard.as_view(), name="admindashboard_view"),
	path('clientdashboard', views.ClientDashboard.as_view(), name="clientdashboard_view"),
	path('clienthome', views.ClientHome.as_view(), name="clienthome_view"),
    path('clientgrades', views.ClientGrades.as_view(), name="clientgrades_view"),
	path('clientvouchers', views.ClientVouchers.as_view(), name="clientvouchers_view"),
	path('donationpage', views.Donation.as_view(), name="donation_view"),

	path('donationdashboard', views.DonationDashboard.as_view(), name="donationdashboard_view"),
	path('success', views.Success.as_view(), name="success_view"),
	path('pointsclient', views.PointsDashBoard.as_view(), name="pointsdasboard_view"),
	path('pointsadmin', views.PointsAdmin.as_view(), name="pointsadmin_view"),
	path('generalvoucher', views.GenVoucher.as_view(), name="genvoucher_view"),

	
]