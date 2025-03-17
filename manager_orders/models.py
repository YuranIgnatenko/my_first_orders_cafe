from django.conf import settings
from django.db import models
from django.utils import timezone


class Order(models.Model):
	id = models.AutoField(primary_key=True)
	table_numbers = models.IntegerField()
	items = models.TextField()
	# items = models.ForeignKey() # link to other model
	total_price = models.FloatField()
	status = models.TextField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def save(self):pass
	def delete(self):pass
	def edit(self):pass
	def calc_sum(self):pass

	def __str__(self):
		return f"{self.id}"