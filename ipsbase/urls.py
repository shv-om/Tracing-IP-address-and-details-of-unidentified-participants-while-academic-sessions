from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/<int:teacher_id>/', views.teacher_view, name='teacher_view'),
    path('students/<int:student_id>/', views.student_view, name='student_view'),
    path('teachers/generate_id/', views.generate_id_view, name='generate_id'),
]