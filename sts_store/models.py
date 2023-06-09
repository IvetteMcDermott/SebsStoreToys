from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 default='category')

    def __str__(self):
        return self.name


class Ware(models.Model):
    name = models.CharField(max_length=60, unique=True, null=False,
                            blank=False)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    new = models.BooleanField(default=False, null=True, blank=True)
    clearance = models.BooleanField(default=False, null=True, blank=True)
    incomming = models.BooleanField(default=False, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                                    default='subcategory')
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    # Function taken from https://www.youtube.com/watch?v=8iCqlFyFu2s
    def get_rating_total(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()

        return 0


class WareImage(models.Model):
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE,
                             related_name='ware_image')
    image = CloudinaryField(default='placeholder', max_length=255,
                            verbose_name='image')
    caption = models.CharField(max_length=254, null=False, blank=False)
