from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, PermissionDenied

from webservices.models import Teacher, Course, Lesson, Slide

from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.base import ObjectDoesNotExist


class CourseForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True)
    startDate = forms.DateTimeField(required=True)
    endDate = forms.DateTimeField()

    class Meta:
        model = Course
        fields = ['teacher', 'name', 'startDate', 'endDate']

class LessonForm(forms.ModelForm):
    course_id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.TextField(max_length=255, required=True)
    description = forms.TextField(max_length=1000)
    position = forms.IntegerField(max_length=100, required=True, widget=forms.HiddenInput())

    class Meta:
        model = Lesson
        fields=['lesson_id', 'position', 'googleStyles']

class SlideForm(forms.ModelForm):
    lesson_id = forms.IntegerField(widget=forms.HiddenInput())
    position = forms.IntegerField(max_length=100, required=True, widget=forms.HiddenInput())
    googleStyles = forms.CharField(max_length=75, required=False)

    class Meta:
        model = Slide
        fields=['lesson_id', 'position', 'googleStyles']