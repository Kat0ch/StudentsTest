from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
