from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignupView, name='signup'),
    path('signup/student/', views.StudentSignupView.as_view(), name='student_signup'),
    path('signup/teacher/', views.TeacherSignupView.as_view(), name='teacher_signup'),

    path('login/', auth_views.LoginView.as_view(), name="login"),
	path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]