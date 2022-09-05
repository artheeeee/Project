from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    def __unicode__(self):
        return self.user.username
        

class RequestDonationBox(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=500, blank=True)
    sub_group = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name

class RequestEnvelope(models.Model):
    name = models.CharField(max_length=100,null=False,blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=200, null=False, blank=True)
    city = models.CharField(max_length=300, null=False, blank=True)
    address = models.CharField(max_length=500, null=False, blank=True)
    sub_group = models.CharField(max_length=500, null=False, blank=True)
    
    def __str__(self):
        return self.name

class ClothingDonation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=200,null=False, blank=True)
    city = models.CharField(max_length=300,null=False, blank=True)
    address = models.CharField(max_length=500,null=False, blank=True)
    cc = models.CharField(max_length=500,null=False, blank=True)
    date = models.CharField(max_length=100,null=False, blank=True)
    time = models.CharField(max_length=500, null=False, blank=True)
    
    def __str__(self):
        return self.name


