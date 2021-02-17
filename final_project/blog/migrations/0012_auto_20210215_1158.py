# Generated by Django 3.1.6 on 2021-02-15 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210215_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_category',
            name='super_category',
        ),
        migrations.AddField(
            model_name='post_category',
            name='SubCategories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='super_category', to='blog.post_category'),
        ),
    ]