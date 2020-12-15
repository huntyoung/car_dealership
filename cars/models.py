import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

def current_year():
    return datetime.date.today().year

class Car(models.Model):

    img = models.ImageField()
    year = models.IntegerField(default=current_year(), validators=[MinValueValidator(1900), MaxValueValidator(current_year() + 1)])
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return str(self.year) + ' ' + str(self.model)
