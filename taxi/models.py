from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return self.username


class Manufacturer(models.Model):
    name = models.CharField(max_length=60, unique=True)
    country = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=60)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver)

    def __str__(self):
        return self.model