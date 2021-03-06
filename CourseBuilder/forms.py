from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, PermissionDenied

from models import Teacher, Course, Lesson, Slide

from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.base import ObjectDoesNotExist


class CourseForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = Course
        fields = ['teacher', 'name']

class LessonForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.Textarea)
    description = forms.CharField(max_length=1000, widget=forms.Textarea, required=False)

    class Meta:
        model = Lesson
        fields=['course', 'name' , 'description']

class SlideForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea, required=False)
    googleStyles = forms.CharField(max_length=75, required=False)

    class Meta:
        model = Slide
        fields=['lesson', 'name', 'content', 'googleStyles']