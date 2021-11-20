from django.db import models

# Create your models here.
class Customer(models.Model):
	name=models.CharField(max_length=200, null=True)
	LastName=models.CharField(max_length=200, null=True)
	Email=models.CharField(max_length=200, null=True)
	Placeofbirth=models.CharField(max_length=200, null=True)
	password=models.CharField(max_length=200, null=True)


class Info(models.Model):
	CHOICES1 = (
			('sedentry','sedentry'),
			('moderately active','moderately active'),
			('active','active'),
)
	CHOICES2 = (
		('weightloss','weightloss'),
		('musclegain','musclegain'),
		('healthyeating','healthyeating'),
	)
	CHOICES3 = (
		('Vegetarian','Vegetarian'),
		('NonVegetarian','NonVegetarian'),
		('Vegan','Vegan'),
	)
	name=models.CharField(max_length=200, null=True)
	age=models.FloatField(null=True)
	height=models.FloatField(null=True)
	weight=models.FloatField(null=True)
	gender=models.CharField(max_length=200, null=True)
	lifestyle=models.CharField(max_length=200, null=True,choices=CHOICES1)
	goals=models.CharField(max_length=200, null=True,choices=CHOICES2)
	foodprefence=models.CharField(max_length=200, null=True,choices=CHOICES3)
	