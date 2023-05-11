# Generated by Django 3.2.18 on 2023-05-09 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sts_store', '0003_alter_wareimage_ware'),
        ('profiles', '0003_auto_20230425_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bookmark', to='profiles.userprofile')),
                ('ware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sts_store.ware')),
            ],
        ),
    ]