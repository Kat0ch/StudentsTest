from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    courses_list = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'birth_day', 'courses_list']

    def get_courses_list(self, obj):
        enrollments = obj.enrolled_student.all()
        courses = Course.objects.filter(enrolled_course__in=enrollments)
        return CourseToStudentSerializer(courses, many=True).data


class CourseToStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'start_date', 'end_date', 'lectures_count']


class CourseSerializer(serializers.ModelSerializer):
    students_list = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'start_date', 'end_date', 'lectures_count', 'students_list']

    def get_students_list(self, obj):
        enrollments = obj.enrolled_course.all()
        students = Student.objects.filter(enrolled_student__in=enrollments)
        return StudentToStudentSerializer(students, many=True).data


class StudentToStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'birth_day']


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student_id', 'course_id', 'enrollment_date']
