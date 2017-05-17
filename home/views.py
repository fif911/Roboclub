from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from blog.models import Article




def index(request):
    model = Article
    context_object_name = 'articles'
    template = loader.get_template('home/index.html')
    articles = Article.objects.all()[:4]
    return render(request, "home/index.html", {"articles": articles})
    # return HttpResponse(template.render(request))
