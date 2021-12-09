from django.db import models


class Address(models.Model):
    street = models.CharField(verbose_name='Street', max_length=100, null=True, blank=False)
    street_number = models.CharField(verbose_name='Street number', max_length=10, null=True, blank=False)
    apartment_number = models.CharField(verbose_name='Apartment number', max_length=10, null=True, blank=True)
    zip_code = models.CharField(verbose_name='ZIP Code', max_length=10, null=True, blank=False)
    city = models.CharField(verbose_name='City', max_length=100, null=True, blank=False)

    def __str__(self):
        return f'{self.city}, ({self.street})'


class Plot(models.Model):
    BUILDIN_PLOT = 0
    AGRICULTURAL_PLOT = 1
    INVESTMENT_PLOT = 2

    PLOT_TYPES = (
        (BUILDIN_PLOT, 'Building'),
        (AGRICULTURAL_PLOT, 'Agricultural'),
        (INVESTMENT_PLOT, 'External'),
    )

    plot_type = models.IntegerField(verbose_name='Plot type', choices=PLOT_TYPES, null=False, blank=False)
    plot_price = models.PositiveSmallIntegerField(verbose_name='Plot price', default=0, null=True, blank=True)
    total_area = models.DecimalField(verbose_name='Total area', max_digits=7, decimal_places=2, null=True,
                                     blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name='Address', null=True, blank=False)

    def __str__(self):
        return f'{self.get_plot_type_display()}, ({self.address.city}, {self.address.street})'


class Realestate(models.Model):
    REALESTATE_MULTI_FAMILY = 0
    REALESTATE_SINGLE_FAMILY = 1

    REALESTATE_TYPES = (
        (REALESTATE_MULTI_FAMILY, 'Multi-family house'),
        (REALESTATE_SINGLE_FAMILY, 'Single-family house')
    )

    KITCHEN_OPEN = 0
    KITCHEN_CLOSED = 1

    KITCHEN = [
        (KITCHEN_OPEN, 'Kitchen open'),
        (KITCHEN_CLOSED, 'Kitchen closed')
    ]

    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, verbose_name='Plot', null=True, blank=False)
    realestate_type = models.IntegerField(verbose_name='Realestete type', choices=REALESTATE_TYPES, null=True,
                                          blank=False)
    realestate_price = models.PositiveSmallIntegerField(default=0, verbose_name='Realestete price', null=True,
                                                        blank=False)
    realestate_area = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Realestete area', null=True,
                                          blank=False)
    number_floors = models.PositiveSmallIntegerField(default=0, verbose_name='Number floors', null=True, blank=False)
    rooms = models.PositiveSmallIntegerField(default=0, verbose_name='Rooms', null=True, blank=True)
    kitchen = models.IntegerField(verbose_name='Kitchen', choices=KITCHEN, null=True, blank=True)
    bathroom = models.PositiveSmallIntegerField(default=0, verbose_name='Bathroom', null=True, blank=True)
    year_built = models.DateField(auto_now_add=False, verbose_name='Year built', null=True, blank=True)
    description = models.TextField(default='', verbose_name='Description', null=True, blank=True)

    def __str__(self):
        return f'{self.get_realestate_type_display()}, ({self.plot.address.city}, {self.plot.address.street})'


class Flat(models.Model):
    realestate = models.ForeignKey(Realestate, on_delete=models.CASCADE, verbose_name='Realestate', null=True,
                                   blank=False)
    floor_number = models.PositiveSmallIntegerField(default=0, verbose_name='Floor number', null=True, blank=True)


class Garage(models.Model):
    NO_GARAGE = 0
    UNDERGROUND_GARAGE = 1
    EXTERNAL_PARKING_SPACE = 2
    DETACHED_GARAGE = 3
    BELONGING_GARAGE = 4

    GARAGE_TYPES = (
        (NO_GARAGE, 'No'),
        (UNDERGROUND_GARAGE, 'Underground'),
        (EXTERNAL_PARKING_SPACE, 'External'),
        (DETACHED_GARAGE, 'Detached'),
        (BELONGING_GARAGE, 'Belonging')
    )

    realestate = models.ForeignKey(Realestate, on_delete=models.CASCADE, verbose_name='Realestate', null=True,
                                   blank=False)
    garage_type = models.IntegerField(verbose_name='Garage type', choices=GARAGE_TYPES, null=True, blank=False)
    garage_price = models.PositiveSmallIntegerField(default=0, verbose_name='Garage price', null=True, blank=False)






