# Generated by Django 4.2 on 2023-04-29 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bullets', '0005_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
