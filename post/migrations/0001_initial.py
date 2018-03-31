# Generated by Django 2.0.3 on 2018-03-30 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_description', models.CharField(max_length=200)),
                ('post_date', models.DateTimeField(default=datetime.datetime.now)),
                ('post_image_url', models.CharField(default='<empty>', max_length=400)),
                ('post_image', models.ImageField(upload_to='static')),
            ],
        ),
    ]
