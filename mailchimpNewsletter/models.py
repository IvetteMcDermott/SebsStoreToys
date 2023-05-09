from django.db import models

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField(null=False, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return str(self.email)
