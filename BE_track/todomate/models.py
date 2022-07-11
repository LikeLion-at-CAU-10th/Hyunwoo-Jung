from django.db import models
from django.forms import CharField, DateField, NullBooleanField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, default="호호" ,blank=None, null=True)
    view_auth = models.IntegerField(default=0,null=True, blank=None)
    color = models.CharField(max_length=10, default='#000000',null=True, blank=None)
    pup_date = models.DateField(auto_now_add=True)