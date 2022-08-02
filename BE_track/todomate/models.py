from random import choices
from unicodedata import category
from django.db import models
from django.forms import CharField, DateField, NullBooleanField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, default="호호" ,blank=None, null=True)
    view_auth = models.IntegerField(default=0,null=True, blank=None)
    color = models.CharField(max_length=10, default='#000000',null=True, blank=None)
    pup_date = models.DateField(auto_now_add=True)
    

class Todo(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False,blank=False)
    content=models.CharField(max_length=50)
    thumb_nail=models.ImageField(upload_to="todo/",null=True,blank=True)
    is_completed=models.BooleanField(default=False)
    pup_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    
class LikeLion(models.Model):
    
    CHOICES=(
        ('기획',"기획"),
        ('백엔드','백엔드'),
        ('프론트','프론트')
        )
    
    name=models.CharField(max_length=20,default="",unique=True)
    age=models.CharField(max_length=20,choices=CHOICES)
    
    
    
    