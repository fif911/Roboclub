from django.conf.urls import url
from . import views

from .views import CourseDetail,CoursesList

urlpatterns = [

    url(r'^courses/(?P<id>\d+)$', CourseDetail.as_view(), name='courseDetail'),
    url(r'^courses/', CoursesList.as_view(), name='coursesList'),



]