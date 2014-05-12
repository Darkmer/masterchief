from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

'''
Database

- Users
  - email
  - password
  - joinDate
  - firstName
  - lastName
  - city
  - state
- Courses
  - course_id
  - name
  - starteDate
  - endDate
- Lessons
  - lesson_id
  - title
  - description
- Slides
  - slide_id
  - lesson_id
  - layoutType (string)
  - slidePosition
- Content
  - slide_id
  - content_id
  - text (html, css)
'''

class Teacher(models.Model):
  teacher_id = models.OneToOneField(User)
  email = models.CharField(max_length=255, unique=True)
  firstName = models.CharField(max_length=50)
  lastName = models.CharField(max_length=50)
  city = models.TextField(max_length=50)
  state = models.TextField(max_length=2)

  def __unicode__(self):
    return self.firstName + " " + self.lastName

class Course(models.Model):
  course_id = models.IntegerField(editable=False, db_index=True)
  teacher = models.ForeignKey(Teacher)
  name = models.TextField(max_length=50)
  startDate = models.DateTimeField()
  endDate = models.DateTimeField()

  def __unicode__(self):
    return self.name

  def startDate_is_before_endDate(self):
    return self.startDate < self.endDate

class Lesson(models.Model):
  lesson_id = models.IntegerField(editable=False, db_index=True)
  course_id = models.ForeignKey(Course)
  teacher_id = models.ForeignKey(Teacher)
  name = models.TextField(max_length=255)
  description = models.TextField(max_length=1000)

  def __unicode__(self):
    return self.name

class Slide(models.Model):
  slide_id = models.IntegerField(editable=False, db_index=True)
  lesson_id = models.ForeignKey(Lesson)
  layoutType = models.TextField(max_length=20)
  slidePosition = models.IntegerField()

class Content(models.Model):
  slide_id = models.ForeignKey(Slide)
  content_id = models.IntegerField(editable=False, db_index=True)
  text = models.TextField()

