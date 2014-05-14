# Some useful stuff to have in your views.py
import json
import CourseBuilder.settings #replace project with the main project folder with settings

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

# Models Imported
from models import Teacher, Course, Lesson, Slide

from forms import CourseForm, LessonForm, SlideForm



def course_admin(request):
    print "course admin called"
    return render(request, 'admin/course.html', {'form': CourseForm(), 'courses' : Course.objects.all(), })

def lesson_admin(request, course_id):
    print "Lesson admin called"
    try:
        course = Course.objects.get(pk=course_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No Course Exists!')

    try:
        lessons = Lesson.objects.filter(course_id=course_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No Slides Exist Yet For This Course')

    return render(request, 'admin/lesson.html', {'course_id': course_id, 'lessons' : lessons.objects.all(), 'form': LessonForm()})

def slide_admin(request, course_id, lesson_id):
	#Allow users to edit slides and ensure template has a slide preview - that would be cool.
    print "slide admin called"
    try:
        course = Course.objects.get(pk=course_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No Course Exists!')

    try:
        slides = Slide.objects.filter(lesson_id=lesson_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No Slides Exist Yet For This Course')

    return render(request, 'admin/slide.html', {
        'course_id': course_id, 
        'lesson_id': lesson_id,
        'slides' : slides.objects.all(), 
        'form': SlideForm()})


#ADMIN AJAX CALLS
@staff_member_required
@require_POST
def course_admin_actions(request, course_id):
    if request.is_ajax():
    	action = request.POST['action'] #action can be 'update', 'remove', 'new'
    pass

@staff_member_required
@require_POST
def lesson_admin_actions(request, lesson_id):
    if request.is_ajax():
    	action = request.POST['action'] #action can be 'update', 'remove', 'new'
    pass

@staff_member_required
@require_POST
def slide_admin_actions(request, slide_id):
    if request.is_ajax():
    	action = request.POST['action'] #action can be 'update', 'remove', 'new'
    pass



#APP USER views
def course_view(request):
    print "course view called"
    try:
        courses = Course.objects.all()	
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No courses exist!')

    return render(request, 'view/course.html', { 'courses': courses })

def about_view(request):
	print "about view called"
	return render(request, 'view/about.html')


def lesson_view(request, course_id):
    print "lesson view called"
    try:
        course = Course.objects.get(pk=course_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No Course Exists!')
    try:
        lessons = Lesson.objects.filter(course_id=course_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No lessons exist yet for this course')

    return render(request, 'view/lesson.html', {'course': course, 'lessons' : lessons.all()})

def slideshow_view(request, course_id, lesson_id):
	#Generate Google SlideShow view for user
    print "slideshow view called " + lesson_id

    try:
        course = Course.objects.get(pk=course_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('This course does not exist')

    try:
        lesson = Lesson.objects.get(pk=lesson_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('This lesson does not exist')

    try:
        slides = Slide.objects.filter(lesson_id=lesson_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No slideshow for this lesson!')

    print slides
    return render(request, 'view/slideshow.html', {'course': course, 'lesson': lesson, 'slides' : slides})

