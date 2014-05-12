from django.contrib import admin
from models import Teacher, Course, Lesson, Slide

# Register your models here.
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(Slide)