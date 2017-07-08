from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Device(models.Model):
	Device_type = models.CharField(max_length=50)
	Brand_name = models.CharField(max_length=100)
	RAM = models.CharField(max_length = 15)
	Storage_size = models.CharField(max_length = 15)
	Screen_size = models.CharField(max_length=10)
	Cost = models.IntegerField()
	Supplier = models.CharField(max_length = 50)
	def __str__(self):
		return self.Device_type

class Customer(models.Model):
	Name = models.CharField(max_length=50)
	def __str__(self):
		return self.Name

class Sale(models.Model):
	Customer_id = models.ForeignKey(Customer)
	Purchase_Date = models.DateTimeField(timezone.now())
	device = models.ForeignKey(Device)
	Amount_Paid = models.IntegerField()

	def __str__(self):
		return self.Brand_name

