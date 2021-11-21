from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class AccountUser(models.Model):
    uid = models.BigAutoField(primary_key = True)
    first_name = models.CharField(max_length = 50) #pwede ma unique
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50, unique = True)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    birthdate = models.DateField()
    username = models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 50)

   

    
# @receiver(post_save, sender=User)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()        

class ContactMessage(models.Model):
    name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 50)
    email = models.CharField(max_length = 150)
    message = models.TextField(null = True)

    def __str__(self):
        return self.email

class Grade(models.Model):
    subject_code = models.CharField(max_length = 20)
    faculty_name = models.CharField(max_length = 100)
    units = models.FloatField()
    midterm = models.FloatField()
    finals = models.FloatField()
    finalgrade = models.FloatField()
    student = models.ForeignKey(AccountUser,to_field='username', on_delete=models.CASCADE)

class ExclusiveVoucher(models.Model):
    ev_id = models.BigAutoField(primary_key = True)
    ev_code = models.IntegerField()
    ev_title = models.CharField(max_length = 20)
    ev_percentage = models.CharField(max_length = 10)
    student = models.ForeignKey(AccountUser,to_field='username', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ev_code)

class GeneralVoucher(models.Model):
    gv_id = models.BigAutoField(primary_key = True)
    gv_code = models.IntegerField() 
    gv_title = models.CharField(max_length = 20)
    gv_percentage = models.CharField(max_length = 10)
    student = models.ForeignKey(AccountUser,to_field='username', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.gv_code)   







