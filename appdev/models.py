from django.db import models
from django.utils.crypto import get_random_string

# Create your models here.

class AccountUser(models.Model):
    idn = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    birthdate = models.DateField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.idn

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

class ExclusiveVoucher(models.Model):
    ev_code = models.IntegerField()

    def __str__(self):
        return str(self.ev_code)

class GeneralVoucher(models.Model):
    gv_code = models.IntegerField() 

    def __str__(self):
        return str(self.gv_code)   







