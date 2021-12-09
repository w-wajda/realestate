from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100, null=True, blank=False)
    street_number = models.CharField(max_length=10, null=True, blank=False)
    apartment_number = models.CharField(max_length=10, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=False)
    city = models.CharField(max_length=60, null=True, blank=False)


class Plot(models.Model):
    total_area = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=False)
    price = models.PositiveSmallIntegerField(default=0, null=True, blank=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)


class Realestate(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, null=True, blank=False, )


class Flat(models.Model):
    realestate = models.ForeignKey(Realestate, on_delete=models.CASCADE, null=True, blank=False)


class Garage(models.Model):
    realestate = models.ForeignKey(Realestate, on_delete=models.CASCADE, null=True, blank=False)


