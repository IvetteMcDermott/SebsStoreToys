from django.db import models
from django.contrib.auth.models import User
from sts_store.models import Ware


class Review(models.Model):
    rating = [
              (1, '1'),
              (2, '2'),
              (3, '3'),
              (4, '4'),
              (5, '5'),
    ]

    ware = models.ForeignKey(Ware, related_name="reviews",
                             on_delete=models.CASCADE)
    body = models.TextField(max_length=300, null=False, blank=False)
    author = models.ForeignKey(User, related_name="author",
                               on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    rating = models.IntegerField(choices=rating, default='5',
                                 null=False, blank=False)

    def __str__(self):
        return f'Review {self.body} by {self.author}'
