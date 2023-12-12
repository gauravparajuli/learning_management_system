from django.urls import path, include
from . import views

urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),

    # teacher
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login/', views.teacher_login),

    # course category
    path('category/', views.CategoryList.as_view()),

    # course
    path('course/', views.CourseList.as_view()),
]

