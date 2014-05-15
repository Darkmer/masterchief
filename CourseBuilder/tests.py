from django.test import TestCase
from django.http import HttpRequest
from models import Teacher, Course, Lesson, Slide
from views import course_view, lesson_view, slideshow_view
from django.contrib.auth.models import User

#Run this command in terminal to run unit tests: "python manage.py test"

def setup(self):
  print "-----in setup"  
  user1 = User(username="test1", email="test1@gmail.com", first_name="john", last_name="smith")
  user2 = User(username="test2", email="test2@gmail.com", first_name="sally", last_name="smith")
  user1.save()
  user2.save()
  
  teacher1 = Teacher()
  teacher1.teacher = user1
  teacher1.save()
  teacher2 = Teacher()
  teacher2.teacher = user2
  teacher2.save()  

  course1 = Course(teacher=teacher1, name="Intro1", position=1)
  course2 = Course(teacher=teacher2, name="Advanced2", position=2)
  course1.save()
  course2.save()
  
  lesson1 = Lesson(course=course1, name="Lesson1", description="Intro1 - Lesson1", position=1)
  lesson2 = Lesson(course=course1, name="Lesson2", description="Intro1 - Lesson2", position=2)
  lesson1.save()
  lesson2.save()

  slide1 = Slide(lesson=lesson1, name="Slide1", content="<h1>Slide1</h1>", position=1, googleStyles=" ")
  slide2 = Slide(lesson=lesson1, name="Slide2", content="<h1>Slide2</h1>", position=2, googleStyles=" ")
  slide1.save()
  slide2.save()

class TeacherMethodTest(TestCase):
  def test_teacher_insert(self):
    print "in test_teacher_insert"
    setup(self)    
    
    self.assertEqual(Teacher.objects.count(), 2)
    user3 = User(username="test3", email="test3@gmail.com", first_name="juan", last_name="garcia")
    user3.save()
    teacher3 = Teacher()
    teacher3.teacher = user3
    teacher3.save()
    self.assertEqual(Teacher.objects.count(), 3)

  def test_teacher_delete(self):
    print "in test_teacher_delete"
    setup(self)

    self.assertEqual(Teacher.objects.count(), 2)
    Teacher.objects.get(pk=1).delete()
    self.assertEqual(Teacher.objects.count(), 1)

class CourseMethodTest(TestCase):	
  def test_course_insert(self):
    print "in test_course_insert"
    setup(self)

    self.assertEqual(Course.objects.count(), 2)
    course3 = Course(teacher=Teacher.objects.get(pk=1), name="Grad3", position=3)
    course3.save()
    self.assertEqual(Course.objects.count(), 3)

  def test_course_delete(self):
    print "in test_course_delete"
    setup(self)

    self.assertEqual(Course.objects.count(), 2)
    Course.objects.get(pk=1).delete()
    self.assertEqual(Course.objects.count(), 1)

  def test_course_reorder(self):
    print "in test_course_reorder"
    setup(self)

    course1 = Course.objects.get(pk=1)
    course2 = Course.objects.get(pk=2)
    x = course1.position < course2.position
    self.assertTrue(x)
    self.assertEqual(Course.objects.count(), 2)

    course1.position = 2
    course2.position = 1
    x = course1.position > course2.position
    self.assertTrue(x)

class LessonMethodTest(TestCase):
  def test_lesson_insert(self):
    print "in test_lesson_insert"
    setup(self)

    self.assertEqual(Lesson.objects.count(), 2)
    lesson3 = Lesson(course=Course.objects.get(pk=1), name="Lesson3", description="Third lesson", position=3)
    lesson3.save()
    self.assertEqual(Lesson.objects.count(), 3)

  def test_lesson_delete(self):
    print "in test_lesson_delete"
    setup(self)

    self.assertEqual(Lesson.objects.count(), 2)
    Lesson.objects.get(pk=1).delete()
    self.assertEqual(Lesson.objects.count(), 1)

  def test_lesson_reorder(self):
    print "in test_lesson_reorder"
    setup(self)
    lesson1 = Lesson.objects.get(pk=1)
    lesson2 = Lesson.objects.get(pk=2)
    x = lesson1.position < lesson2.position
    self.assertTrue(x)
    self.assertEqual(Lesson.objects.count(), 2)
    
    lesson1.position = 2
    lesson2.position = 1
    x = lesson1.position > lesson2.position
    self.assertTrue(x)

class SlideMethodTest(TestCase):
  def test_slide_insert(self):
    print "in test_slide_insert"
    setup(self)

    self.assertEqual(Slide.objects.count(), 2)
    slide3 = Slide(lesson=Lesson.objects.get(pk=1), name="Slide3", content="<h1>Slide3</h1>", position=3, googleStyles=" ")
    slide3.save()
    self.assertEqual(Slide.objects.count(), 3)

  def test_slide_delete(self):
    print "in test_slide_delete"
    setup(self)
    self.assertEqual(Slide.objects.count(), 2)
    Slide.objects.get(pk=1).delete()
    self.assertEqual(Slide.objects.count(), 1)  

  def test_slide_reorder(self):
    print "in test_slide_reorder"
    setup(self)
    slide1 = Slide.objects.get(pk=1)
    slide2 = Slide.objects.get(pk=2)
    x = slide1.position < slide2.position
    self.assertTrue(x)
    self.assertEqual(Slide.objects.count(), 2)

    slide1.position = 2
    slide2.position = 1
    x = slide1.position > slide2.position
    self.assertTrue(x)

class ControllerTest(TestCase):
  def test_course_view(self):
    print "in test_course_view"
    setup(self)
    request = HttpRequest()
    request.user = User.objects.get(pk=1)
    response = course_view(request)
    self.assertIn(b'<h3 class="panel-title">Currently Available Courses</h3>', response.content)

  def test_lesson_view(self):
    print "in test_lesson_view"
    setup(self)
    request = HttpRequest()
    request.user = User.objects.get(pk=1)
    response = lesson_view(request, 1)
    self.assertIn(b' - Lessons</h1>', response.content)

  def test_slideshow_view(self):
    print "in test_slideshow_view"
    setup(self)
    request = HttpRequest()
    request.user = User.objects.get(pk=1)
    response = slideshow_view(request, 1, 1)
    self.assertIn(b'<div class="slide">', response.content)  
