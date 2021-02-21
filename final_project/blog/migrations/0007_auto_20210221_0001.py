# Generated by Django 3.1.6 on 2021-02-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210220_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=500),
        ),
    ]
