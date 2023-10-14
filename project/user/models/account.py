from django.db import models

class Account(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=150, blank=True, null=False)
    profile_img =models.TextField(blank=True, null=True)
