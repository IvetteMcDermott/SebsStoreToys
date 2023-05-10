from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.


class NewsBlog(models.Model):
    title = models.CharField(max_length=60, unique=True, null=False,
                             blank=False)
    image = CloudinaryField(default='placeholder', max_length=255,
                            verbose_name='image')
    description = models.TextField()
    source = models.URLField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
