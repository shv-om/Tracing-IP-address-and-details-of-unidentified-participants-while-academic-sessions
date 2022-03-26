from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import forms

from registration import models as registered_models

from django.contrib.auth.decorators import login_required, user_passes_test
from .decorators import teacher_required, student_required, admin_teacher_required

import random
import string


def index(request):
	return render(request, 'index.html')


# Students Views

@login_required
@student_required
def student_view(request, student_id):

	students = registered_models.Student.objects.get(user_id=request.user.id)

	context_processors={
                    'students': students,
                }
	
	return render(request, 'students_view.html', context_processors)



# Teachers Views

@login_required
@teacher_required
def teacher_view(request, teacher_id):

	teachers = registered_models.Teacher.objects.get(user_id=request.user.id)

	context_processors={
					'teachers': teachers,
				}

	return render(request, 'teachers_view.html', context_processors)


# Generating Ids

def generate_ids():

	random_id = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

	return random_id


@login_required
@admin_teacher_required
def generate_id_view(request):

	rusers = registered_models.User.objects.filter(is_student=True)

	current_user = registered_models.IPadd_RanID.objects.update_or_create(ruser=request.user, defaults={'random_id': generate_ids()})
	users_ids = [current_user[0]]

	for u in rusers:

		ids = registered_models.IPadd_RanID.objects.update_or_create(ruser=u, defaults={'random_id': generate_ids()})

		users_ids.append(ids[0])

	# sid = models.RandomID.objects.filter(ruser_id=ruser.pk)
	# rusers.append(request.user)

	# users_ids = zip(sid, rusers)

	context_processors = {
					'users_ids': users_ids,
				}

	return render(request, 'generate_id_view.html', context_processors)


@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def admin_view(request):
	allusers = registered_models.IPadd_RanID.objects.all()

	context_processors = {
					'allusers': allusers,
				}

	return render(request, 'admin_view.html', context_processors)
