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
    course_id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(max_length=255, required=True, widget=forms.Textarea)
    description = forms.CharField(max_length=1000, widget=forms.Textarea)
    position = forms.IntegerField(required=True, widget=forms.HiddenInput())

    class Meta:
        model = Lesson
        fields=['course_id', 'name' , 'description' , 'position']

class SlideForm(forms.ModelForm):
    lesson_id = forms.IntegerField(widget=forms.HiddenInput())
    title = forms.CharField(max_length=255, widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)
    position = forms.IntegerField(required=True, widget=forms.HiddenInput())
    googleStyles = forms.CharField(max_length=75, required=False)

    class Meta:
        model = Slide
        fields=['lesson_id', 'title', 'content', 'position', 'googleStyles']