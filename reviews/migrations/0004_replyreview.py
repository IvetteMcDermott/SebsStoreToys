# Generated by Django 3.2.18 on 2023-05-16 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0003_auto_20230514_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_content', models.TextField()),
                ('replied_date', models.DateTimeField(auto_now_add=True)),
                ('replier_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reply_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='reviews.review')),
            ],
        ),
    ]
