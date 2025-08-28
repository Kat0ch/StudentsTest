from django.urls import path
from .views import *

urlpatterns = [
    path('courses/stats/', CoursesStats.as_view(), name='courses_stats'),

    path('courses/', CoursesList.as_view(), name='courses_list'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroy.as_view(), name='course'),

    path('students/', StudentsList.as_view(), name='students_list'),
    path('students/<int:pk>/', StudentsRetrieveUpdateDestroy.as_view(), name='student'),
]
