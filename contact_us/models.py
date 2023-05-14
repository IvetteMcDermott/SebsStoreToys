from django.db import models

# Create your models here.


class ContactUs(models.Model):

    subject = [
              ('product', 'About a product'),
              ('services', 'About our services'),
              ('order', 'About an order'),
              ('delivery', 'About delivery'),
              ('enquiry', 'General enquiry'),
              ('Claim or Complain', 'Claim or Complain'),
    ]

    email = models.EmailField(null=False, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False)
    subject = models.CharField(max_length=30, choices=subject,
                               null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Subject {self.subject} by {self.email} on {self.date}'
