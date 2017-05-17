from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.views.generic.list import ListView

# Create your models here.
class F_report(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    nameOfDocument1=models.CharField(max_length=250,null=True, blank=True,)
    document1 = models.URLField(max_length=150,null=True, blank=True, )
    nameOfDocument2 = models.CharField(max_length=250,null=True, blank=True,)
    document2 = models.URLField(max_length=150, null=True, blank=True, )
    nameOfDocument3 = models.CharField(max_length=250,null=True, blank=True,)
    document3 = models.URLField(max_length=150, null=True, blank=True, )
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __unicode__(self):
        return u"%s" % self.title