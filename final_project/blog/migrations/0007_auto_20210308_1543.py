# Generated by Django 3.1.6 on 2021-03-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210308_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_category',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]