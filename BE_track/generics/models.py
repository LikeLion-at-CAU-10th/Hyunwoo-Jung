from django.db import models

# Create your models here.
class Generics (models.Model):
    CHOICES = (
        ("에시공", "에시공"),
        ("소프트", "소프트"),
    )
    name = models.CharField(max_length=20, default="", unique=True)
    part = models.CharField(max_length=20, choices=CHOICES, default="백엔드")
    age = models.IntegerField(default=20)
    bio = models.TextField(default="소개를 입력하라.", null=True)
    profile_image = models.ImageField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.name