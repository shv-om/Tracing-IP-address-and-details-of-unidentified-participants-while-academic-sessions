from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.views.generic import CreateView

from . import forms
from . import models

from ipsbase import views as baseviews

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from ipsbase.decorators import admin_teacher_required


@login_required
@admin_teacher_required
# @user_passes_test(lambda u: u.is_superuser or u.is_teacher or u.is_staff)
def SignupView(request):
	return render(request, 'registration/signup.html', {})


@method_decorator(admin_teacher_required, name='dispatch')
class StudentSignupView(CreateView):
	model = models.User
	form_class = forms.StudentSignupForm
	template_name = 'registration/students_signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'student'
		return super().get_context_data(**kwargs)

	def form_valid(self, forms):
		user = forms.save()
		login(self.request, user)
		return redirect(baseviews.student_view, user.id)


@method_decorator(admin_teacher_required, name='dispatch')
class TeacherSignupView(CreateView):
	model = models.User
	form_class = forms.TeacherSignupForm
	template_name = 'registration/teacher_signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'teacher'
		return super().get_context_data(**kwargs)

	def form_valid(self, forms):
		user = forms.save()
		login(self.request, user)
		return redirect(baseviews.teacher_view, user.id)

