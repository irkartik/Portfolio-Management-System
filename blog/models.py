from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	created_by = models.ForeignKey(User)
	post_title = models.CharField(max_length=250)
	brief = models.CharField(max_length=5000)
	body = models.TextField()
	created_on = models.DateTimeField(default=datetime.now)

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.post_title

class Like(models.Model):
	user = models.ForeignKey(User, related_name='liked_by')
	post = models.ForeignKey(Post)
	created = models.DateTimeField(default = datetime.now)