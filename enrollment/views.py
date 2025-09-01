from django.db.models import Avg, Count, Sum, QuerySet
from rest_framework.request import Request
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializers import CourseSerializer, StudentSerializer, SendMessageSerializer
from django.utils.decorators import method_decorator
from .services import CustomLimitOffsetPagination
from .tasks import send_message
from django.views.decorators.cache import cache_page


@method_decorator(cache_page(5 * 60), name='dispatch')
class CoursesStats(APIView):
    def get(self):
        average_students: Enrollment = Enrollment.objects.values('course_id').annotate(
            count=Count('student_id')
        ).aggregate(avg_students=Avg('count'))['avg_students']
        most_popular_course: Course = Course.objects.annotate(num_students=Count('enrolled_course')).order_by(
            '-num_students').first()
        total_lectures_count: Course = Course.objects.aggregate(sum_lectures=Sum('lectures_count'))['sum_lectures']

        data: dict = {
            'average_students': average_students or 0,
            'most_popular_course': CourseSerializer(most_popular_course).data if most_popular_course else None,
            'total_lectures_count': total_lectures_count or 0
        }

        return Response(data)


@method_decorator(cache_page(2 * 60), name='dispatch')
class CoursesList(ListCreateAPIView):
    serializer_class: CourseSerializer = CourseSerializer
    queryset: QuerySet = Course.objects.all()
    pagination_class: CustomLimitOffsetPagination = CustomLimitOffsetPagination


class CourseRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset: QuerySet = Course.objects.all()
    serializer_class: CourseSerializer = CourseSerializer


@method_decorator(cache_page(2 * 60), name='dispatch')
class StudentsList(ListCreateAPIView):
    serializer_class: StudentSerializer = StudentSerializer
    queryset: QuerySet = Student.objects.all()
    pagination_class: CustomLimitOffsetPagination = CustomLimitOffsetPagination


class StudentsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset: QuerySet = Student.objects.all()
    serializer_class: StudentSerializer = StudentSerializer


@method_decorator(cache_page(1 * 60), name='dispatch')
class SendMessage(APIView):
    def post(self, request: Request):
        serializer = SendMessageSerializer(data=request.data)
        if serializer.is_valid():
            recipient = serializer.validated_data['recipient']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']

            send_message(recipient, subject, message)
            return Response(serializer.data)
        return Response({'Error': 'Invalid input data'}, status=HTTP_400_BAD_REQUEST)
