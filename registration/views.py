from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from . import forms
from . import models

from ipsbase import views as baseviews

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from ipsbase.decorators import admin_teacher_required, teacher_required

from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from django.contrib.sessions.models import Session


# Preventing Multi-logins from one User
# while logging in and creating new Session Key, Delete all the previous key for that user

@receiver(user_logged_in)
def remove_other_session(sender, user, request, **kwargs):
	
	# removing other session
	s = Session.objects.filter(usersession__user=user).delete()

	# Saving new session
	request.session.save()

	models.UserSession.objects.get_or_create(user=user, sessionkey_id=request.session.session_key)
	print("Session key: ", request.session.session_key)


# Sign-up and Login Views

@login_required
#@user_passes_test(lambda u: u.is_superuser or u.is_teacher)
@admin_teacher_required
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
		# logout(self.request)
		# login(self.request, user)
		return redirect(baseviews.student_view, user.id)


@method_decorator(admin_teacher_required, name='dispatch')
# @user_passes_test(lambda u: u.is_superuser or u.is_staff)
class TeacherSignupView(CreateView):

	model = models.User
	form_class = forms.TeacherSignupForm
	template_name = 'registration/teacher_signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'teacher'
		return super().get_context_data(**kwargs)

	def form_valid(self, forms):
		user = forms.save()
		# logout(self.request)
		# login(self.request, user)
		return redirect(baseviews.teacher_view, user.id)


def user_login(request):

	ipadd = get_user_ip(request)
	print("IP:", ipadd)

	if not request.user.is_authenticated:
		
		if request.method == 'POST':
			loginform = AuthenticationForm(request, request.POST)

			if loginform.is_valid():
				username = loginform.cleaned_data['username']
				passwd = loginform.cleaned_data['password']
				user = authenticate(username=username, password=passwd)

				if user is not None:
					logout(request)
					login(request, user)

					sip = models.IPadd_RanID.objects.update_or_create(ruser=user, defaults={'ipaddress': ipadd})

					return redirect(baseviews.index)

		else:
			loginform = AuthenticationForm()

		context_processors = {
						'form': loginform,
					}

		return render(request, 'registration/login.html', context_processors)

	else:
		return redirect(baseviews.index)


def get_user_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')

	return ip
