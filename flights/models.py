from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Flight(models.Model):
	destination = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="countries")
	time = models.TimeField()
	price = models.DecimalField(max_digits=10, decimal_places=3)
	miles = models.PositiveIntegerField()

	def __str__(self):
		return "to %s at %s" % (self.to.name, str(self.time))


class Booking(models.Model):
	flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="bookings")
	date = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="bookings")
	number_of_travellers = models.PositiveIntegerField()
	miles = models.PositiveIntegerField(default=0)

	def __str__(self):
		return "%s: %s" % (user.username, str(flight))

