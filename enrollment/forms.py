from django.forms import ModelForm
from .models import *


class CreateCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
