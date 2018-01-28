from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	post_title = models.CharField(max_length=250)
	brief = models.TextField(max_length=1000)
	body = RichTextField()
	created_on = models.DateTimeField(default=datetime.now)
	publish = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.post_title

class Like(models.Model):
	user = models.ForeignKey(User, related_name='liked_by', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	created = models.DateTimeField(default = datetime.now)
