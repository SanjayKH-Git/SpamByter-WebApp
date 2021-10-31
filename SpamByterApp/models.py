from django.db import models

# Create your models here.
class GenUsers(models.Model):
    email = models.CharField(max_length=100)
    PhoneNo = models.CharField(max_length=13)
    password = models.CharField(max_length=30)

class SpamUsers(models.Model):
    email = models.CharField(max_length=200)
    PhoneNo = models.CharField(max_length=13)


