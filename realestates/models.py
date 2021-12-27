from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Address(models.Model):
    street = models.CharField(verbose_name='Street', max_length=100)
    street_number = models.CharField(verbose_name='Street number', max_length=10)
    zip_code = models.CharField(verbose_name='ZIP Code', max_length=10)
    city = models.CharField(verbose_name='City', max_length=100)

    def __str__(self):
        return f'{self.city}, ({self.street} {self.street_number})'

    class Meta:
        verbose_name_plural = 'addresses'


class Plot(models.Model):
    BUILDIN_PLOT = 0
    AGRICULTURAL_PLOT = 1
    INVESTMENT_PLOT = 2

    PLOT_TYPES = (
        (BUILDIN_PLOT, 'Building plot'),
        (AGRICULTURAL_PLOT, 'Agricultural plot'),
        (INVESTMENT_PLOT, 'Investment plot'),
    )

    type = models.IntegerField(verbose_name='Plot type', choices=PLOT_TYPES)
    total_area = models.DecimalField(verbose_name='Total plot area', max_digits=7, decimal_places=2, null=True,
                                     blank=True)

    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name='Plot address')

    def __str__(self):
        return f'{self.get_type_display()}, ({self.address.city}, {self.address.street} {self.address.street_number})'


class Garage(models.Model):
    NO_GARAGE = 0
    UNDERGROUND_GARAGE = 1
    EXTERNAL_PARKING_SPACE = 2
    DETACHED_GARAGE = 3
    BELONGING_GARAGE = 4

    GARAGE_TYPES = (
        (NO_GARAGE, 'No garage'),
        (UNDERGROUND_GARAGE, 'Underground'),
        (EXTERNAL_PARKING_SPACE, 'External'),
        (DETACHED_GARAGE, 'Detached'),
        (BELONGING_GARAGE, 'Belonging')
    )

    type = models.IntegerField(verbose_name='Garage type', choices=GARAGE_TYPES)
    parking_number = models.PositiveSmallIntegerField(verbose_name='Parking space number')

    def __str__(self):
        return f'{self.realestate.plot.address.city}, ({self.realestate.plot.address.street}' \
               f' {self.realestate.plot.address.street_number}, space number: {self.parking_number})'


class Realestate(models.Model):
    REALESTATE_MULTI_FAMILY = 0
    REALESTATE_SINGLE_FAMILY = 1

    REALESTATE_TYPES = (
        (REALESTATE_MULTI_FAMILY, 'Multi-family house'),
        (REALESTATE_SINGLE_FAMILY, 'Single-family house')
    )

    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, verbose_name='Plot')

    type = models.IntegerField(verbose_name='Realestete type', choices=REALESTATE_TYPES)
    area = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Total realestete area', null=True,
                               blank=True)
    number_floors = models.PositiveSmallIntegerField(verbose_name='Number floors')
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, verbose_name='Garage')
    year_built = models.DateField(verbose_name='Year built')

    def __str__(self):
        return f'{self.get_type_display()}, ({self.plot.address.city}, {self.plot.address.street}' \
               f' {self.plot.address.street_number})'


class Flat(models.Model):
    BALCONY = 0
    LOGGIA = 1
    TERRACE = 2

    BALCONY_TYPES = (
        (BALCONY, 'Balcony'),
        (LOGGIA, 'Loggia'),
        (TERRACE, 'Terrace')
    )

    KITCHEN_OPEN = 0
    KITCHEN_CLOSED = 1

    KITCHEN = (
        (KITCHEN_OPEN, 'Open'),
        (KITCHEN_CLOSED, 'Closed')
    )

    realestate = models.ForeignKey(Realestate, on_delete=models.CASCADE, verbose_name='Realestate')

    floor_number = models.PositiveSmallIntegerField(verbose_name='Floor number')
    apartment_number = models.CharField(max_length=10, verbose_name='Apartment number')
    rooms = models.PositiveSmallIntegerField(verbose_name='Number of rooms')
    kitchen_type = models.IntegerField(verbose_name='Kitchen type', choices=KITCHEN)
    bathroom = models.PositiveSmallIntegerField(verbose_name='Number of bathroom')
    balcony_type = models.IntegerField(verbose_name='Balcony type', choices=BALCONY_TYPES, null=True, blank=False)

    def __str__(self):
        return f'{self.realestate.plot.address.city}, ({self.realestate.plot.address.street}' \
               f' {self.realestate.plot.address.street_number}/{self.apartment_number})'





class Offer(models.Model):
    SALE = 0
    LEASE = 1

    OFFER_TYPES = [
        (SALE, 'Sale'),
        (LEASE, 'Lease')
    ]

    type = models.IntegerField(verbose_name='Offer type', choices=OFFER_TYPES)
    price = models.PositiveSmallIntegerField(verbose_name='Price')
    description = models.TextField(verbose_name='Description')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.get_type_display()








