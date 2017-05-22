from django.db import models

from django.conf import settings
def upload_location(instance, filename):
    return "%s/%s" %(instance.title,filename)

# Create your models here.
class BlogData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)

    width_field = models.IntegerField(default=0)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id','-time_stamp']