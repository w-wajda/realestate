from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100, null=True, blank=False)
    street_number = models.CharField(max_length=10, null=True, blank=False)
    apartment_number = models.CharField(max_length=10, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=False)
    city = models.CharField(max_length=60, null=True, blank=False)

    def address_description(self):
        return f'{self.city}, ({self.street})'

    def __str__(self):
        return self.address_description()


class Realestate(models.Model):
    KITCHEN = [
        ('OPEN', 'open'),
        ('CLOSED', 'closed')
    ]
    GARAGE = [
        ('YES', 'yes'),
        ('NO', 'no'),
    ]
    city = models.CharField(max_length=60, null=True, blank=False)
    area = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=False)
    area_land = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=False)
    price = models.PositiveSmallIntegerField(default=0, null=True, blank=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    rooms = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    kitchen = models.CharField(max_length=6, null=True, blank=True, choices=KITCHEN)
    bathroom = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    number_floors = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    year_built = models.DateField(auto_now_add=False, null=True, blank=True)
    garage = models.CharField(max_length=3, null=True, blank=True, choices=GARAGE)
    description = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f'{self.city}, {self.area} m2'


class Flat(models.Model):
    KITCHEN = [
        ('OPEN', 'open'),
        ('CLOSED', 'closed')
    ]
    GARAGE = [
        ('YES', 'yes'),
        ('NO', 'no'),
    ]
    city = models.CharField(max_length=60, null=True, blank=False)
    area = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=False)
    price = models.PositiveSmallIntegerField(default=0, null=True, blank=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    rooms = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    kitchen = models.CharField(max_length=6, null=True, blank=True, choices=KITCHEN)
    bathroom = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    number_floors = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    floor_number = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    year_built = models.DateField(auto_now_add=False, null=True, blank=True)
    garage = models.CharField(max_length=3, null=True, blank=True, choices=GARAGE)
    description = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f'{self.city}, {self.area} m2'


class Plot(models.Model):
    total_area = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=False)
    price = models.PositiveSmallIntegerField(default=0, null=True, blank=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    realestate = models.ForeignKey(Realestate, on_delete=models.CASCADE)













