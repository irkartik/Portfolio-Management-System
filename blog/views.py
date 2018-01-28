from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from core.models import *
from django.views.generic import View

from .models import *

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'blog/home.html'
	context_object_name = 'all_posts'

	def get_queryset(self):
		return Post.objects.filter(publish=True).order_by('-created_on')[:40]

	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super(IndexView, self).get_context_data(**kwargs)
	    # Add in a QuerySet of all the books
	    context['social'] = Social.objects.all()
	    return context




class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super(DetailView, self).get_context_data(**kwargs)
	    # Add in a QuerySet of all the books
	    context['social'] = Social.objects.all()
	    return context