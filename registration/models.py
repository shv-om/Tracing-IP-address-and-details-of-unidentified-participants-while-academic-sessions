from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.sessions.models import Session


class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
	grade = models.CharField(max_length=3)


class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
	subject = models.CharField(max_length=20)


class UserSession(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	sessionkey = models.OneToOneField(Session, on_delete=models.CASCADE)


class IPadd_RanID(models.Model):
	ruser = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
	random_id = models.CharField(max_length=8, default=None, null=True)
	ipaddress = models.GenericIPAddressField(null=True)

