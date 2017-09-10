from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
from blog.models import *
# Create your views here.


def homeview(request):
	home_skills = HomeSkills.objects.all()
	social = Social.objects.all()
	certification = Certification.objects.order_by('order')[:6]
	skills = Skill.objects.order_by('order')[:6]
	academics = Academic.objects.order_by('-order')
	work = WorkExperience.objects.order_by('-order')
	profile = Profile.objects.order_by('order')
	quotes = Quote.objects.all()
	projects = Project.objects.all()
	contact = ContactDetails.objects.all()
	post = Post.objects.order_by('-created_on')[:5]
	misctext = MiscText.objects.all()

	context = {
		'home_skills': home_skills,
		'social' : social,
		'certification': certification,
		'skills' : skills,
		'work' : work,
		'academics': academics,
		'profile' : profile,
		'quotes' : quotes,
		'projects' : projects,
		'contact' : contact,
		'posts': post,
		'misctext': misctext
	}
	print('social')
	return render(request, "home/home.html", context)
