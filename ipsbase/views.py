from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models
from . import forms

from registration import models as registered_models

from django.contrib.auth.decorators import login_required
from .decorators import teacher_required, student_required

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
@teacher_required
def generate_id_view(request):

	rusers = registered_models.User.objects.all()

	for u in rusers:
		if u.pk not in models.RandomID.objects.all().values_list('pk', flat=True):
			ids = models.RandomID.objects.create(ruser_id=u.pk, random_id=generate_ids())
			ids.save()

		else:
			ids = models.RandomID.objects.get(ruser_id=u.pk)
			ids.random_id = generate_ids()
			ids.save(update_fields=['random_id'])

	sid = models.RandomID.objects.all()

	users_ids = zip(sid, rusers)

	context_processors = {
					'users_ids': users_ids,
				}

	return render(request, 'generate_id_view.html', context_processors)



