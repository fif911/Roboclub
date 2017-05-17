from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(allow_unicode=True, max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    image2 = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    image3 = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    image4 = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    image5 = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    image6 = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    image7 = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    image8 = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    image9 = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    image10 = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    video1 = models.URLField(max_length=150,null=True, blank=True, )
    video2 = models.URLField(max_length=150,null=True, blank=True, )
    video3 = models.URLField(max_length=150,null=True, blank=True, )

    def get_absolute_url(self):
        return reverse("article", kwargs={"pk": self.pk})

    class Meta:
        ordering = ('-publish',)

    def __unicode__(self):
        return u"%s" % self.slug

    def __unicode__(self):
        return u"%s" % self.title


    def __str__(self):
        return self.title