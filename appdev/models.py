from django.db import models

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
        return self.email

class ContactMessage(models.Model):
    name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 50)
    email = models.CharField(max_length = 150)
    message = models.TextField(null = True)

    def __str__(self):
        return self.email