from django.conf.urls import include, url
from . import views

from .views import ArticlesList, ArticleDetail
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    url(r'^news$', ArticlesList.as_view(), name='articles'),
    # url(r'^news/article/(?P<pk>\d+)/$', ArticleDetail.as_view(), name='article'),
    url(r'^news/(?P<slug>[-\w]+)/$', ArticleDetail.as_view(), name='article'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),


]