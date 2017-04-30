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

    photo1 = ProcessedImageField(blank=True, upload_to='blog/photo1/%Y/%M/%D',
                                processors=[Thumbnail(800,800)],
                                format='JPEG',
                                options={'quality':100})

    photo2 = ProcessedImageField(blank=True, upload_to='blog/photo2/%Y/%M/%D',
                                processors=[Thumbnail(800,800)],
                                format='JPEG',
                                options={'quality':100})

    summary = models.CharField(max_length=200)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.id])

    class Meta:
        ordering = ['id']