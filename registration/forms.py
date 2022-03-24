from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from . import models

class StudentSignupForm(UserCreationForm):
	grade = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta(UserCreationForm.Meta):
		model = models.User

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_student = True
		user.save()

		student = models.Student.objects.create(user=user)
		student.grade = self.cleaned_data.get('grade')
		student.save(update_fields=['grade'])

		return user


class TeacherSignupForm(UserCreationForm):
	subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta(UserCreationForm.Meta):
		model = models.User

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_teacher = True
		user.save()

		teacher = models.Teacher.objects.create(user=user)
		teacher.subject = self.cleaned_data.get('subject')
		teacher.save(update_fields=['subject'])

		return user
