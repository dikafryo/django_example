# Generated by Django 4.2 on 2023-04-28 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bullets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bullets',
            new_name='Board',
        ),
        migrations.RenameModel(
            old_name='BulletComment',
            new_name='Comment',
        ),
    ]
