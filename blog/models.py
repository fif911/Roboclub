from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from image_cropping import ImageRatioField
def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=250)
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    preview_image = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    cropping = ImageRatioField('preview_image', '480x480')
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, )
    cropping1 = ImageRatioField('image', '480x480')
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



    # Then override models save method:
    def save(self, *args, **kwargs):
        self.cropping = ""
        self.cropping1 = ""
        if not self.id:
            # Only set the slug when the object is created.
            self.slug = slugify(self.title)  # Or whatever you want the slug to use
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-publish',)

    def __unicode__(self):
        return u"%s" % self.slug

    def __unicode__(self):
        return u"%s" % self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})

