from django.db import models
# Create your models here.

class HomeSkills(models.Model):
	name = models.CharField(max_length=1000)

	class Meta:
		verbose_name = "Home Skill"
		verbose_name_plural = "Home Skills"
	def __str__(self):
		return self.name

class ContactDetails(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	website = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	mobile = models.CharField(max_length=100)
	address = models.TextField()

	def __str__(self):
		return self.name

class MiscText(models.Model):
	about_text = models.TextField()
	profile_text = models.TextField()
	skill_text = models.TextField()
	certification_text = models.TextField()
	contact_text = models.TextField()
	resume_url = models.CharField(max_length=1000)
	profilepic_url = models.CharField(max_length=1000)


class Social(models.Model):
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=1000)

	class Meta: 
		verbose_name = "Social"
		verbose_name_plural = "Social"

	def __str__(self):
		return self.name

class Skill(models.Model):
	name = models.CharField(max_length=100)
	proficiency = models.IntegerField()
	order = models.PositiveIntegerField(default=1, null =False, blank = False)

	def __str__(self):
		return self.name

class Certification(models.Model):
	name = models.CharField(max_length=1000)
	provider = models.CharField(max_length=1000)
	url = models.CharField(max_length=1000)
	order = models.PositiveIntegerField(default=1, null =False, blank = False)

	class Meta:
		verbose_name= "Certification"
		verbose_name_plural = "Certifications"

	def __str__(self):
		return self.name

class Profile(models.Model):
	profile_topic = models.CharField(max_length=100)
	value = models.CharField(max_length=1000)
	order = models.PositiveIntegerField()

	def __str__(self):
		return self.profile_topic

class WorkExperience(models.Model):
	position = models.CharField(max_length=100)
	organization = models.CharField(max_length=1000)
	start_date = models.CharField(max_length=100)
	end_date = models.CharField(max_length=100)
	description = models.TextField()
	certificate = models.CharField(max_length=10000, verbose_name="Certificate Link (google drive)")
	order = models.PositiveIntegerField()


	class Meta:
		verbose_name = "Work Experience"
		verbose_name_plural = "Work Experiences"

	def __str__(self):
		return self.organization

class Academic(models.Model):
	institution = models.CharField(max_length=1000)
	degree = models.CharField(max_length=1000)
	start_date = models.CharField(max_length=100)
	end_date = models.CharField(max_length=100)
	description = models.TextField()
	marksheet = models.CharField(max_length=1000)
	order = models.PositiveIntegerField()

	class Meta:
		verbose_name = "Academic"

	def __str__(self):
		return self.institution

class Quote(models.Model):
	text = models.TextField()
	citiation = models.CharField(max_length=100)

	def __str__(self):
		return self.text

class Project(models.Model):
	name = models.CharField(max_length=1000)
	github_url = models.CharField(max_length=1000)
	url = models.CharField(max_length=1000)
	tech = models.CharField(max_length=10000, verbose_name="Technology Stack Used")
	description = models.TextField()
	image_url = models.CharField(max_length=10000)

	def __str__(self):
		return self.name


