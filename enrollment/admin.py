from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


class EnrollmentAdmin(admin.ModelAdmin):
    pass


# FIXME: регать лучше декораторами, так код не размазывается по всеми файлу,
#  т.к. этих админок может быть 50+ в одном файле, не хочется за ними тут ползать везде
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
