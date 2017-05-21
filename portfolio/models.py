#portfolio/models.py
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.core.urlresolvers import reverse


# Create your models here.
class TimestampModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Post(TimestampModel):
    title = models.CharField(max_length=100)
    category= models.CharField(max_length=100,
        choices = (
            ('Electronic-Eng','Electronic-Eng'),
            ('Start-up','Start-up'),
            ('Project','Project'),
            ('Experience','Experience'),
        ),default=False)

    photo1 = models.ImageField(blank=True, upload_to='blog/photo1/%Y/%M/%D')

    photo2 = models.ImageField(blank=True, upload_to='blog/photo2/%Y/%M/%D')

    summary = models.CharField(max_length=200)

    period = models.CharField(max_length=200, default=False)

    url = models.CharField(max_length=100)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.id])

    class Meta:
        ordering = ['id']