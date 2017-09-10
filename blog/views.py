from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.views.generic import View

from .models import *

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'blog/home.html'
	context_object_name = 'all_posts'

	def get_queryset(self):
		return Post.objects.order_by('-created_on')[:40]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'