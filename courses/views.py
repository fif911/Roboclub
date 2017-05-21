from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import *
# Create your views here.
class CoursesList(TemplateView):
    template_name = "courses/courses_list.html"

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()

        return render(request, self.template_name, {'courses': courses})

class CourseDetail(TemplateView):
    template_name = "courses/course.html"
    # def get(self, request, *args, **kwargs):
    #     id = kwargs['id']
    #     course = Course.objects.get(id=id)
    #     return render(request, self.template_name,{"course": course})
    def get_context_data(self, **kwargs):
        context = super(CourseDetail, self).get_context_data(**kwargs)
        context['course'] = Course.objects.get(id=kwargs['id'])
        return context

