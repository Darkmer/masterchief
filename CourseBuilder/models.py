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

  def __unicode__(self):
    return self.firstName + " " + self.lastName

class Course(models.Model):
  teacher = models.ForeignKey(Teacher)
  name = models.TextField(max_length=50)
  startDate = models.DateTimeField()
  endDate = models.DateTimeField()

  def __unicode__(self):
    return self.name

  def startDate_is_before_endDate(self):
    return self.startDate < self.endDate

class Lesson(models.Model):
  course_id = models.ForeignKey(Course)
  name = models.TextField(max_length=255)
  description = models.TextField(max_length=1000)
  position = models.IntegerField()

  def __unicode__(self):
    return self.name

class Slide(models.Model):
  lesson_id = models.ForeignKey(Lesson)
  position = models.IntegerField()
  googleStyles = models.CharField(max_length=75)

class Content(models.Model):
  slide_id = models.ForeignKey(Slide)
  text = models.TextField()

