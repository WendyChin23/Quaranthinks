from django.contrib import admin
from .models import AccountUser, ContactMessage, Grade

# Register your models here.

class ContactDashboard(admin.ModelAdmin):
	list_display = ('email','id','name', 'subject', 'message')
	list_filter = ['subject']
	search_fields = ['email']


class GradeDashboard(admin.ModelAdmin):
	list_display = ('id', 'subject_code', 'faculty_name', 'units', 'midterm', 'finals', 'finalgrade')
	list_filter = ['faculty_name']
	search_fields = ['subject_code']

admin.site.register(AccountUser)
admin.site.register(ContactMessage, ContactDashboard)
admin.site.register(Grade, GradeDashboard)

