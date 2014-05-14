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

  def __unicode__(self):
    return self.name

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
  content = models.TextField(null=True)
  position = models.IntegerField()
  googleStyles = models.CharField(max_length=75, null=True)

  def __unicode__(self):
    return self.title
