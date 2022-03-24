from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
	grade = models.CharField(max_length=3)


class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
	subject = models.CharField(max_length=20)
