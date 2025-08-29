from django.forms import ModelForm
from .models import *
from django import forms


class CreateCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class MailForm(forms.Form):
    email = forms.EmailField()
