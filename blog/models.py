from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=50)
	pub_date = models.DateTimeField()
	body = models.TextField(max_length=500)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return list(self.body.split())[:16]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
