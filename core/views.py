from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import *
from blog.models import *
from django.core.mail import send_mail, EmailMessage
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
	post = Post.objects.filter(publish=True).order_by('-created_on')[:5]
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
	return render(request, "home/home.html", context)

def sendEmail(request):
	if request.method == 'POST':
		name = request.POST.get('contactName')
		from_email = request.POST.get('contactEmail')
		subject = request.POST.get('contactSubject')
		message = request.POST.get('contactMessage')

		message = "<" + name + ">" + " has sent you the following message " + "on the subject " + "<" + subject + ">" + " and says the message " + "<" + message + ">" + " his email ID is " + "<" + from_email +">"
		send_mail(subject, message, 'raazu889@gmail.com', ['rajujha373@gmail.com'], fail_silently=False)
		
	# #.info(request, 'Your password has been changed successfully!')
	# context = {
	# 	'name' : name,
	# 	'email' : from_email,
	# 	'subject': subject,
	# 	'message': message,
	# }
	return redirect('emailSent') #render(request, "home/thankyou.html", context)

def emailSent(request):
	social = Social.objects.all()
	context= {
		'social' : social,
	}
	return render(request, "home/thankyou.html", context)


