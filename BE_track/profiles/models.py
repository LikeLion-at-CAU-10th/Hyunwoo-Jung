from django.db import models
from django.forms import CharField, DateField, NullBooleanField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50, default="현우" ,blank=None, null=True)
    age = models.IntegerField(default=0,null=True, blank=None)
    phone = models.IntegerField(default=0,null=True, blank=None)
    
    
class Content(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=False,blank=False)
    content=models.CharField(max_length=50)
    
