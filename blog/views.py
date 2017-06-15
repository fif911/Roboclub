# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import Article
from django.http import Http404




class ArticlesList(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = 'articles'

    def get(self, request, *args, **kwargs):

        articles = Article.objects.all()
        # Отбираем первые 12 статей
        paginator = Paginator(articles, 12)
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
    # def get_queryset(self, request):


class ArticleDetail(ListView):

    template_name = "blog/articles_detail.html"

    def get(self, request, *args, **kwargs):
        article_detail=Article.objects.get(slug=kwargs['slug'])
        return render(request,self.template_name, {"article": article_detail})
    # raise Http404("No MyModel matches the given")
    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['article'] = Article.objects.get(pk=kwargs['pk'])
        return context


