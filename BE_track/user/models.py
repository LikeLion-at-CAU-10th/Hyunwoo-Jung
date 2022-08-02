from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

class ServiceUserManager(UserManager):
    def _create_user(self,username,email,password,**extra_fields):
        if not username:
            raise ValueError("username을 입력하세요")


# Create your models here.
class ServiceUser(AbstractUser):
    phone = models.CharField(max_length=11,default="01000000000")
  