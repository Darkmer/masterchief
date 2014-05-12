from django.test import TestCase
from models import Course
import datetime

class CourseMethodTest(TestCase):
	
	def test_startDate_is_before_endDate(self):
		course = Course(startDate = datetime.date.today(), endDate = datetime.date.today() + datetime.timedelta(days=1))
		self.assertEqual(course.startDate_is_before_endDate(), True)

'''
class TeacherMethodTest(TestCase):

class LessonMethodTest(TestCase):

class SlideMethodTest(TestCase):

class ContentMethodTest(TestCase):
'''