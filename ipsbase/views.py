from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models

from registration import models as registered_models

from django.contrib.auth.decorators import login_required
from .decorators import teacher_required, student_required

def index(request):
	return render(request, 'index.html')


@login_required
@student_required
def student_view(request, id):

	students = registered_models.Student.objects.get(id=request.user.id)

	context_processors={
                    'students': students,
                }
	
	return render(request, 'students_view.html', context_processors)


@login_required
@teacher_required
def teacher_view(request, teacher_id):

	teachers = registered_models.Teacher.objects.get(id=request.user.id)

	context_processors={
					'teachers': teachers,
				}

	return render(request, 'teachers_view.html', context_processors)

