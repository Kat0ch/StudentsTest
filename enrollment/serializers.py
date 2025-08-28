from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    courses_list = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'birth_day', 'courses_list']

    def get_courses_list(self, obj):
        courses = obj.enrolled_student.all()
        return StudentSerializer(courses, many=True).data


class CourseSerializer(serializers.ModelSerializer):
    students_list = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'start_date', 'end_date', 'lectures_count', 'students_list']

    def get_students_list(self, obj):
        students = obj.enrolled_course.all()
        return StudentSerializer(students, many=True).data


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student_id', 'course_id', 'enrollment_date']
