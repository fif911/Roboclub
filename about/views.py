from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import F_report

class ArticlesList(ListView):
    model = F_report
    template_name = "about/financial_reports.html"
    context_object_name = 'articles'
    def get(self, request, *args, **kwargs):
        articles = F_report.objects.all()

        paginator = Paginator(articles, 5)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            articles = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {"articles": articles})


def comments(request):
    template = loader.get_template('about/comments.html')

    return HttpResponse(template.render(request))

def team(request):
    template = loader.get_template('about/team.html')

    return HttpResponse(template.render(request))

def index(request):
    template = loader.get_template('about/index.html')

    return HttpResponse(template.render(request))

def mission(request):
    template = loader.get_template('about/mission.html')

    return HttpResponse(template.render(request))
def partners(request):
    template = loader.get_template('about/partners.html')

    return HttpResponse(template.render(request))

# def financial_reports(request):
#     template = loader.get_template('about/financial_reports.html')
#
#     return HttpResponse(template.render(request))
