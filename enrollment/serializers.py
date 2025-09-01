from django.db.models import QuerySet
from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    courses_list: serializers.SerializerMethodField = serializers.SerializerMethodField()

    class Meta:
        model: Student = Student
        fields: list = ['id', 'name', 'birth_day', 'courses_list']

    def get_courses_list(self, obj):
        courses: QuerySet = Student.objects.filter(enrolled_course__in=obj.enrolled_student.all()).distinct()
        return CourseToStudentSerializer(courses, many=True).data


class CourseToStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Course = Course
        fields: list = ['id', 'name', 'start_date', 'end_date', 'lectures_count']


class CourseSerializer(serializers.ModelSerializer):
    students_list: serializers.SerializerMethodField = serializers.SerializerMethodField()

    class Meta:
        model: Course = Course
        fields: list = ['id', 'name', 'start_date', 'end_date', 'lectures_count', 'students_list']

    def get_students_list(self, obj):
        students: QuerySet = Student.objects.filter(enrolled_student__in=obj.enrolled_course.all()).distinct()
        return StudentToStudentSerializer(students, many=True).data


class StudentToStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Student = Student
        fields: list = ['id', 'name', 'birth_day']


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Enrollment = Enrollment
        fields: list = ['id', 'student_id', 'course_id', 'enrollment_date']


class SendMessageSerializer(serializers.Serializer):
    recipient: serializers.EmailField = serializers.EmailField()
    subject: serializers.CharField = serializers.CharField(max_length=50)
    message: serializers.CharField = serializers.CharField()


class CoursesStatsSerializer(serializers.Serializer):
    average_students = serializers.FloatField()
    most_popular_course = serializers.CharField()
    total_lectures_count = serializers.IntegerField()
