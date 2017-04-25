#portfolio/models.py
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

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
                                processors=[Thumbnail(500,500)],
                                format='JPEG',
                                options={'quality':60})

    photo2 = ProcessedImageField(blank=True, upload_to='blog/photo2/%Y/%M/%D',
                                processors=[Thumbnail(500,500)],
                                format='JPEG',
                                options={'quality':60})

    summary = models.CharField(max_length=200)