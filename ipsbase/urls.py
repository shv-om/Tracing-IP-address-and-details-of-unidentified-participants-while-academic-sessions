from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/<int:teacher_id>/', views.teacher_view, name='teacher_view'),
    path('students/<int:id>/', views.student_view, name='student_view'),
]