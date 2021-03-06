from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
def upload_location(instance, filename):#FIXXX
    return ("courses/"+"%s/%s" % (instance.id, filename))

class Course(models.Model):

    name = models.CharField(max_length=100,default=None)
    age_limit = models.FloatField(null=True, blank=True,)
    course_objective = models.TextField(null=True, blank=True, )
    body = models.TextField(null=True, blank=True, )
    # description = models.CharField(widget=widgets.AdminWYMEditor)

    image = models.ImageField(upload_to=upload_location, null=True, blank=True, )#FIXXXXX


    def get_absolute_url(self):
        return reverse("courseDetail", kwargs={"id": self.id})


    def __str__(self):
        return self.name

