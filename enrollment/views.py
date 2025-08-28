from django.db.models import Avg, Count, Max, Sum
from django.views.generic import ListView, CreateView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .forms import *
from django.views.decorators.cache import cache_page
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .serializers import CourseSerializer, StudentSerializer
from django.utils.decorators import method_decorator


@method_decorator(cache_page(5 * 60), name='dispatch')
class CoursesStats(APIView):
    def get(self, request):
        average_students = \
            Enrollment.objects.values('course_id').annotate(count=Count('student_id')).aggregate(
                avg_students=Avg('count'))[
                'avg_students']
        most_popular_course = Course.objects.annotate(num_students=Count('enrolled_course')).order_by(
            '-num_students').first()
        total_lectures_count = Course.objects.aggregate(sum_lectures=Sum('lectures_count'))['sum_lectures']

        data = {
            'average_students': average_students or 0,
            'most_popular_course': CourseSerializer(most_popular_course).data if most_popular_course else None,
            'total_lectures_count': total_lectures_count or 0
        }

        return Response(data)


@method_decorator(cache_page(2 * 60), name='dispatch')
class CoursesList(ListView):
    paginate_by = 10
    template_name = 'enrollment/courses_list.html'
    model = Course


class CourseRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentsList(ListView):
    paginate_by = 10
    template_name = 'enrollment/students_list.html'
    model = Student


class StudentsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
