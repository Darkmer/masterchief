# Some useful stuff to have in your views.py
import json
import CourseBuilder.settings #replace project with the main project folder with settings

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

# Models Imported
from models import Teacher, Course, Lesson, Slide

from forms import CourseForm, LessonForm, SlideForm

from django.forms.formsets import formset_factory


def course_admin(request):
    print "course admin called"
    # instance = get_object_or_404(Coworkers, id=id)
    max_num = Course.objects.count()
    course_set = formset_factory(CourseForm, extra=max_num, max_num=max_num)

    keys = [c.pk for c in Course.objects.order_by('position').all()]
    forms = course_set(initial=Course.objects.order_by('position').all().values())
    forms = zip(forms, keys)
    return render(request, 'admin/course.html', {'forms': forms, 'emptyForm': CourseForm(), 'courses' : Course.objects.order_by('position').all() })

def lesson_admin(request, course_id):
    print "Lesson admin called"
    try:
        course = Course.objects.get(pk=course_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No Course Exists!')

    try:
        lessons = Lesson.objects.filter(course_id=course_id)
        max_num = Lesson.objects.count()
        lesson_set = formset_factory(LessonForm, extra=max_num, max_num=max_num)

        keys = [c.pk for c in Lesson.objects.order_by('position').all()]
        forms = lesson_set(initial=Lesson.objects.order_by('position').all().values())
        forms = zip(forms, keys)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No Slides Exist Yet For This Lesson')


    return render(request, 'admin/lesson.html', {'forms': forms, 'emptyForm': LessonForm(), 'lessons' : Lesson.objects.order_by('position').all() })

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
def course_admin_update(request, course_id, prefix):
    if request.is_ajax():
        form = CourseForm(request.POST) if prefix == 'None' else CourseForm(request.POST, prefix=prefix) 
        if form.is_valid():
            try:
                course = Course.objects.get(pk=course_id)
                course.teacher = form.cleaned_data['teacher']
                course.name = form.cleaned_data['name'] 
                course.save()
                return HttpResponse('OK')
                
            except ObjectDoesNotExist:
                # create new object
                position = None
                if Course.objects.count() > 0:
                    course = Course.objects.order_by('-position').all()[0]
                    position = course.position

                else:
                    position = 1

                newcourse = Course()
                newcourse.teacher = form.cleaned_data['teacher']
                newcourse.name = form.cleaned_data['name']
                newcourse.position = position
                newcourse.save()
                return HttpResponse('OK')
        else:
            errors_dict = {}
            if form.errors:
                for error in form.errors:
                    e = form.errors[error]
                    field = prefix+"-"+error;
                    errors_dict[field] = unicode(e)
            print errors_dict
            return HttpResponseBadRequest(json.dumps(errors_dict))
    else:
        return HttpResponseNotFound('You do not have permission to access this page!')

@staff_member_required
@require_POST
def course_admin_delete(request, course_id):
    if request.is_ajax():
        course = Course.objects.get(pk=course_id);
        course.delete();
        return HttpResponse('OK')
    else:
        return HttpResponseNotFound('You do not have permission to access this page!')


@staff_member_required
@require_POST
def course_admin_reorder(request):
    if request.is_ajax():
        courselist = request.POST.getlist('subjectlist[]');
        print courselist
        for order, course_id in enumerate(courselist):     
            course = Course.objects.get(pk=course_id);
            course.position = order + 1;
            course.save()
        return HttpResponse('OK')
    else:
        return HttpResponseNotFound('You do not have permission to access this page!')




#ADMIN AJAX CALLS
@staff_member_required
@require_POST
def lesson_admin_update(request, lesson_id, prefix):
    if request.is_ajax():
        form = lessonForm(request.POST) if prefix == 'None' else lessonForm(request.POST, prefix=prefix) 
        if form.is_valid():
            try:
                lesson = lesson.objects.get(pk=lesson_id)
                lesson.description = form.cleaned_data['description']
                lesson.name = form.cleaned_data['name'] 
                lesson.save()
                return HttpResponse('OK')
                
            except ObjectDoesNotExist:
                # create new object
                position = None
                if lesson.objects.count() > 0:
                    lesson = lesson.objects.order_by('-position').all()[0]
                    position = lesson.position

                else:
                    position = 1

                newlesson = lesson()
                newlesson.name = form.cleaned_data['name']
                newlesson.description = form.cleaned_data['description']
                newlesson.position = position
                newlesson.save()
                return HttpResponse('OK')
        else:
            errors_dict = {}
            if form.errors:
                for error in form.errors:
                    e = form.errors[error]
                    field = prefix+"-"+error;
                    errors_dict[field] = unicode(e)
            print errors_dict
            return HttpResponseBadRequest(json.dumps(errors_dict))
    else:
        return HttpResponseNotFound('You do not have permission to access this page!')

@staff_member_required
@require_POST
def lesson_admin_delete(request, lesson_id):
    if request.is_ajax():
        lesson = lesson.objects.get(pk=lesson_id);
        lesson.delete();
        return HttpResponse('OK')
    else:
        return HttpResponseNotFound('You do not have permission to access this page!')


@staff_member_required
@require_POST
def lesson_admin_reorder(request):
    if request.is_ajax():
        lessonlist = request.POST.getlist('subjectlist[]');
        print lessonlist
        for order, lesson_id in enumerate(lessonlist):     
            lesson = lesson.objects.get(pk=lesson_id);
            lesson.position = order + 1;
            lesson.save()
        return HttpResponse('OK')
    else:
        return HttpResponseNotFound('You do not have permission to access this page!')


























#APP USER views
def course_view(request):
    print "course view called"
    courseList = Course.objects.order_by()[:2]	
    return render(request, 'view/course.html', { 'courseList': courseList })

def lesson_view(request, course_id):
    print "lesson view called"
    return render(request, 'view/lesson.html', {'course_id': course_id})

def slideshow_view(request, course_id, lesson_id):
	#Generate Google SlideShow view for user
    print "slideshow view called"
    return render(request, 'view/slideshow.html', {'course_id': course_id, 'lesson_id': lesson_id})

