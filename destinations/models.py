from django.db import models
import uuid
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
# Create your models here.

class Destinations(models.Model):
	Category = [
    ('Religious', 'religious'),
    ('Hilly', 'hilly'),
    ('Mountain', 'mountain'),
    ('Terai', 'terai'),
    ('FamousDestination', 'famousdestination'),
    ('JungleSafari', 'junglesafari'),
    ]

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name= models.CharField(max_length=50, null=False, blank=True)
	picture = models.FileField(upload_to='images',default='images/default_image.jpg', blank=True, null=True)
	description= models.CharField(max_length=200, null=True)
	Created_date= models.DateField(auto_now_add=True)
	price= models.IntegerField(null=True,blank=True)
	category= models.CharField(max_length=20, choices=Category, null=False, blank=False)


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)


	def __str__(self):
		return self.name


class Bookings(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE)
	destinations= models.ForeignKey(Destinations, on_delete=models.CASCADE, related_name='destinations')
	date= models.DateField(auto_now_add=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('bookingdetails', args=[str(self.id)])

	def __str__(self):
		return str(self.id)

class Galary(models.Model):
	title: models.CharField(max_length=40, null=True, blank=True)
	image: models.ImageField(upload_to='images/')

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title



class Messages(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE)
	name= models.CharField(max_length=50, null=False, blank=True)
	mail= models.EmailField(null=False, blank=True)
	number= models.BigIntegerField(blank=True)
	mesge= models.CharField(max_length=200, null=False, blank=True)
	date= models.DateField(auto_now_add=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		
	def __str__(self):
		return str(self.id)