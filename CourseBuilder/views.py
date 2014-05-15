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
    courses = Course.objects.order_by('position').all()


    keys = [(c.pk, c.teacher_id) for c in courses]
    forms = course_set(initial=courses.values())
    forms = zip(forms, keys)
    return render(request, 'admin/course.html', {
        'forms': forms, 
        'emptyForm': CourseForm(), 
        'courses' : Course.objects.order_by('position').all() })


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
                response = {'created_object_id': newcourse.pk}
                return HttpResponse(json.dumps(response), mimetype="application/json") 
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



def lesson_admin(request, course_id):
    print "Lesson admin called"
    try:
        course = Course.objects.get(pk=course_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No Course Exists!')

    lessons = Lesson.objects.filter(course_id=course_id).order_by('position')
    max_num = Lesson.objects.count()
    lesson_set = formset_factory(LessonForm, extra=max_num, max_num=max_num)

    keys = [c.pk for c in lessons]
    forms = lesson_set(initial=lessons.values())
    forms = zip(forms, keys)


    return render(request, 'admin/lesson.html', {
                'page_course_id': course.pk, 
                'page_course_name': course.name, 
                'forms': forms, 
                'emptyForm': LessonForm(), 
                'lessons' : lessons})



@staff_member_required
@require_POST
def lesson_admin_update(request, lesson_id, prefix):
    if request.is_ajax():
        form = LessonForm(request.POST) if prefix == 'None' else LessonForm(request.POST, prefix=prefix) 
        if form.is_valid():
            try:
                lesson = Lesson.objects.get(pk=lesson_id)
                lesson.course = form.cleaned_data['course']
                lesson.description = form.cleaned_data['description']
                lesson.name = form.cleaned_data['name'] 
                lesson.save()
                return HttpResponse('OK')
                
            except ObjectDoesNotExist:
                # create new object
                position = None
                if Lesson.objects.count() > 0:
                    lesson = Lesson.objects.order_by('-position').all()[0]
                    position = lesson.position

                else:
                    position = 1

                newlesson = Lesson()
                newlesson.course = form.cleaned_data['course']
                newlesson.name = form.cleaned_data['name']
                newlesson.description = form.cleaned_data['description']
                newlesson.position = position
                newlesson.save()
                response = {'created_object_id': newlesson.pk}
                return HttpResponse(json.dumps(response), mimetype="application/json") 
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
        lesson = Lesson.objects.get(pk=lesson_id);
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
            lesson = Lesson.objects.get(pk=lesson_id);
            lesson.position = order + 1;
            lesson.save()
        return HttpResponse('OK')
    else:
        return HttpResponseNotFound('You do not have permission to access this page!')





def slide_admin(request, course_id, lesson_id):
    #Allow users to edit slides and ensure template has a slide preview - that would be cool.
    print "slide admin called"
    try:
        course = Course.objects.get(pk=course_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No Course Exists!')

    try:
        lesson = Lesson.objects.get(pk=lesson_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('No Slides Exist Yet For This Course')

    slides = Slide.objects.filter(lesson_id=lesson_id).order_by('position')
    max_num = Slide.objects.count()
    slides_set = formset_factory(SlideForm, extra=max_num, max_num=max_num)

    keys = [c.pk for c in slides]
    forms = slides_set(initial=slides.values())
    forms = zip(forms, keys)

    return render(request, 'admin/slide.html', {
        'page_course_id': course.pk, 
        'page_course_name': course.name, 
        'page_lesson_id': lesson.pk, 
        'page_lesson_name': lesson.name, 
        'forms': forms, 
        'slides' : slides, 
        'emptyForm': SlideForm()
        })

@staff_member_required
@require_POST
def slide_admin_update(request, slide_id, prefix):
    if request.is_ajax():
        form = SlideForm(request.POST) if prefix == 'None' else SlideForm(request.POST, prefix=prefix) 
        if form.is_valid():
            try:
                slide = Slide.objects.get(pk=slide_id)
                slide.lesson = form.cleaned_data['lesson']
                slide.content = form.cleaned_data['content']
                slide.googleStyles = form.cleaned_data['googleStyles']
                slide.name = form.cleaned_data['name'] 
                slide.save()
                return HttpResponse('OK')
                
            except ObjectDoesNotExist:
                # create new object
                position = None
                if Slide.objects.count() > 0:
                    slide = Slide.objects.order_by('-position').all()[0]
                    position = slide.position

                else:
                    position = 1

                newslide = Slide()
                newslide.lesson = form.cleaned_data['lesson']
                newslide.name = form.cleaned_data['name']
                newslide.content = form.cleaned_data['content']
                newslide.googleStyles = form.cleaned_data['googleStyles']
                newslide.position = position
                newslide.save()
                response = {'created_object_id': newslide.pk}
                return HttpResponse(json.dumps(response), mimetype="application/json") 
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
def slide_admin_delete(request, slide_id):
    if request.is_ajax():
        slide = Slide.objects.get(pk=slide_id);
        slide.delete();
        return HttpResponse('OK')
    else:
        return HttpResponseNotFound('You do not have permission to access this page!')


@staff_member_required
@require_POST
def slide_admin_reorder(request):
    if request.is_ajax():
        slidelist = request.POST.getlist('subjectlist[]');
        print slidelist
        for order, slide_id in enumerate(slidelist):     
            slide = Slide.objects.get(pk=slide_id);
            slide.position = order + 1;
            slide.save()
        return HttpResponse('OK')
    else:
        return HttpResponseNotFound('You do not have permission to access this page!')

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

def tutorial_view(request):
	print "tutorial view called"
	return render(request, 'view/tutorial.html')

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
    print "slideshow view called "

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

