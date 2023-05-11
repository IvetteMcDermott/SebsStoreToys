# Generated by Django 3.2.18 on 2023-05-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=60)),
                ('subject', models.CharField(choices=[('product', 'About a product'), ('services', 'About our services'), ('order', 'About an order, please include the number of this one in the mail'), ('delivery', 'About delivery'), ('enquiry', 'General enquiry'), ('Claim or Complain', 'Claim or Complain')], max_length=30)),
                ('description', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
