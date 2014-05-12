from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Teacher(models.Model):
  teacher = models.OneToOneField(User)

  def __unicode__(self):
    return self.teacher.first_name + " " + self.teacher.last_name

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
  title = models.TextField(max_length=255)  
  content = models.TextField()
  position = models.IntegerField()
  googleStyles = models.CharField(max_length=75)

  def __unicode__(self):
    return self.title
