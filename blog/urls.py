from django.conf.urls import include, url
from . import views
#from .views import ArticlesList, ArticleDetail, HomeTemplate ,TagIndexView
from .views import ArticlesList, ArticleDetail

urlpatterns = [
    url(r'^news$', ArticlesList.as_view(), name='articles'),
    url(r'^news/article/(?P<pk>\d+)/$', ArticleDetail.as_view(), name='article'),
    url(r'^news/article/(?P<slug>[-\w]+)/$', ArticleDetail.as_view(), name='article'),


]