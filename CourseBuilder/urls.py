from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ADMIN COURSE MANAGEMENT TOOL
urlpatterns += patterns('CourseBuilder.views',
    url(r'^course_management/$', 'course_admin', name="course_admin"),
    url(r'^course_management/(?P<course_id>\d+)/lessons/$', 'lesson_admin', name="lesson_admin"),
    url(r'^course_management/(?P<course_id>\d+)/lessons/(?P<lesson_id>\d+)/$', 'slide_admin', name="slide_admin"),
    # AJAX URLS
    url(r'^course_admin_update/(?P<course_id>\d+)/(?P<prefix>.+)/$', 'course_admin_update', name="course_admin_update"),
    url(r'^course_admin_delete/(?P<course_id>\d+)/$', 'course_admin_delete', name="course_admin_delete"),
    url(r'^course_admin_reorder/$', 'course_admin_reorder', name="course_admin_reorder"),
    

    url(r'^lesson_admin_actions/(?P<lesson_id>\d+)/$', 'lesson_admin_actions', name="lesson_admin_actions"),
    url(r'^slide_admin_actions/(?P<slide_id>\d+)/$', 'slide_admin_actions', name="slide_admin_actions"),
)


# USER COURSE VIEW
urlpatterns += patterns('CourseBuilder.views',
    url(r'^courses/$', 'course_view', name="course_view"),
    url(r'^courses/(?P<course_id>\d+)/lessons/$', 'lesson_view', name="lesson_view"),
)