# Generated by Django 3.1.6 on 2021-03-08 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210228_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_category',
            old_name='super_category',
            new_name='sub_category',
        ),
    ]