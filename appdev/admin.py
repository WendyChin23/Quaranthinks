from django.contrib import admin
from .models import AccountUser, ContactMessage

# Register your models here.

class ContactDashboard(admin.ModelAdmin):
	list_display = ('email','name', 'subject', 'message')
	list_filter = ['subject']
	search_fields = ['email']

admin.site.register(AccountUser)
admin.site.register(ContactMessage, ContactDashboard)
