from django.db import models
from django.urls import reverse

# Create your models here.
class Pet(models.Model):
	name = models.CharField(max_length=120)
	age = models.IntegerField()
	available= models.BooleanField(default=True) 
	image= models.ImageField(upload_to='pet_image', null=True, blank=True)
	price= models.DecimalField(max_digits=10, decimal_places=3)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('pet-detail' ,kwargs={'pet_id':self.id})