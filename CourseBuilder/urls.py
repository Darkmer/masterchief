from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls"))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ADMIN COURSE MANAGEMENT TOOL
urlpatterns += patterns('CourseBuilder.views',
    url(r'^course_management/$', 'course_admin', name="course_admin"),
    url(r'^course_management/(?P<course_id>\d+)/lessons/$', 'lesson_admin', name="lesson_admin"),
    url(r'^course_management/(?P<course_id>\d+)/lessons/(?P<lesson_id>\d+)/$', 'slide_admin', name="slide_admin"),
    # AJAX URLS
    (r'^course_admin_actions/$', 'course_admin_actions'),
    (r'^lesson_admin_actions/$', 'lesson_admin_actions'),
    (r'^slide_admin_actions/$', 'slide_admin_actions'),
)


# USER COURSE VIEW
urlpatterns += patterns('CourseBuilder.views',
    url(r'^courses/$', 'course_view', name="course_view"),
    url(r'^courses/(?P<course_id>\d+)/lessons/$', 'lesson_view', name="lesson_view"),
    url(r'^courses/(?P<course_id>\d+)/lessons/(?P<lesson_id>\d+)/$', 'slideshow_view', name="slideshow_view"),
)

# ABOUT VIEW
urlpatterns += patterns('CourseBuilder.views',
	url(r'^about/', 'about_view', name="about_view")
)

