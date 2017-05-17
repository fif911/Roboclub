from django.conf.urls import url

from . import views
from .views import ArticlesList
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^comments$', views.comments, name='comments'),
    url(r'^team$', views.team, name='team'),
    url(r'^mission$', views.mission, name='mission'),
    url(r'^partners$', views.partners, name='partners'),
    # url(r'^financial_reports$', views.financial_reports, name='financial_reports'),
    url(r'^financial_reports$', ArticlesList.as_view(), name='articles'),
]