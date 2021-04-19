from django.db import models



# Create your models re.
class Users(models.Model):
	first_name = models.CharField(max_length = 264,unique = True)
	last_name = models.CharField(max_length = 264,unique = True)
	email = models.EmailField(max_length = 264,unique = True)

	def __str__(self):
		return self.first_name