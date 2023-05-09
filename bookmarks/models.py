from django.db import models
from sts_store.models import Ware
from profiles.models import UserProfile


class Bookmarks(models.Model):
    """ Save bookmarks and possible save a comment or reminder on """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             related_name='user_bookmark',
                             null=False, blank=False)
    ware = models.ForeignKey(
        Ware, on_delete=models.CASCADE, null=False, blank=False)
    tag = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.ware.name
