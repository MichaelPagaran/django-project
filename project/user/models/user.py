from django.db import models
from .account import Account

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=150, null=False, blank=True)
    lastname = models.CharField(max_length=150, null=False, blank=True)
    birthdate = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    accounts = models.ManyToManyField(Account)