# Generated by Django 4.0.5 on 2022-06-08 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_remove_post_header_image_post_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_image',
            new_name='image',
        ),
    ]