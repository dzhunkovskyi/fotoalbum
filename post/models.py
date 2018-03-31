from django.db import models

# Create your models here.

from datetime import datetime


class Post(models.Model):

	post_title = models.CharField(max_length=200)
	post_description = models.CharField(max_length=200)
	post_date = models.DateTimeField(default=datetime.now)
	post_image_url = models.CharField(default='<empty>', max_length=400)
	post_image = models.ImageField(upload_to='static')
	# post_video_url = models.CharField(default='', max_length=400)
	# post_video = models.ImageField(upload_to='static')