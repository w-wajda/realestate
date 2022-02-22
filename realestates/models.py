from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from gfklookupwidget.fields import GfkLookupField


class Client(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20)
    surname = models.CharField(verbose_name='Surname', max_length=50)
    email = models.EmailField(verbose_name='Email')
    mobile_number = models.CharField(verbose_name='Mobile number', max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Client'
        unique_together = ['name', 'surname', 'email', 'mobile_number']


class Address(models.Model):
    street = models.CharField(verbose_name='Street', max_length=100)
    street_number = models.CharField(verbose_name='Street number', max_length=10)
    zip_code = models.CharField(verbose_name='ZIP Code', max_length=10, null=True, blank=True)
    city = models.CharField(verbose_name='City', max_length=100)

    def __str__(self):
        return f'{self.city}, {self.street} {self.street_number}'

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        unique_together = ['street', 'street_number', 'city']


class Plot(models.Model):
    BUILDIN_PLOT = 0
    AGRICULTURAL_PLOT = 1
    INVESTMENT_PLOT = 2

    PLOT_TYPES = (
        (BUILDIN_PLOT, 'Building plot'),
        (AGRICULTURAL_PLOT, 'Agricultural plot'),
        (INVESTMENT_PLOT, 'Investment plot'),
    )

    type_plot = models.IntegerField(verbose_name='Plot type', choices=PLOT_TYPES)
    total_area_plot = models.DecimalField(verbose_name='Total plot area', max_digits=7, decimal_places=2, null=True,
                                          blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name='Plot address')

    def __str__(self):
        return f'{self.address.city}, {self.address.street} {self.address.street_number}'

    class Meta:
        verbose_name = 'Plot'


class Realestate(models.Model):
    REALESTATE_MULTI_FAMILY = 0
    REALESTATE_SINGLE_FAMILY = 1

    REALESTATE_TYPES = (
        (REALESTATE_MULTI_FAMILY, 'Multi-family house'),
        (REALESTATE_SINGLE_FAMILY, 'Single-family house')
    )

    plot = models.OneToOneField(Plot, on_delete=models.CASCADE, verbose_name='Plot address')
    type_realestate = models.IntegerField(verbose_name='Realestete type', choices=REALESTATE_TYPES)
    number_floors = models.PositiveSmallIntegerField(verbose_name='Number floors')
    year_built = models.DateField(verbose_name='Year built')

    def __str__(self):
        return f'{self.get_type_realestate_display()}, ({self.plot.address.city}, {self.plot.address.street}' \
               f' {self.plot.address.street_number})'

    class Meta:
        verbose_name = 'Realestate'


class Flat(models.Model):
    BALCONY = 0
    LOGGIA = 1
    TERRACE = 2
    NO_BALCONY = 3

    BALCONY_TYPES = [
        (BALCONY, 'Balcony'),
        (LOGGIA, 'Loggia'),
        (TERRACE, 'Terrace'),
        (NO_BALCONY, 'No balcony')
    ]

    KITCHEN_OPEN = 0
    KITCHEN_CLOSED = 1

    KITCHEN = [
        (KITCHEN_OPEN, 'Open'),
        (KITCHEN_CLOSED, 'Closed')
    ]

    realestate = models.ForeignKey(Realestate, on_delete=models.CASCADE, verbose_name='Realestate')
    area = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Total realestete area', default='0')
    floor_number = models.PositiveSmallIntegerField(verbose_name='Floor number')
    apartment_number = models.CharField(max_length=10, verbose_name='Apartment number', null=True, blank=True)
    rooms = models.PositiveSmallIntegerField(verbose_name='Number of rooms')
    kitchen_type = models.IntegerField(verbose_name='Kitchen type', choices=KITCHEN)
    bathroom = models.PositiveSmallIntegerField(verbose_name='Number of bathroom')
    balcony_type = models.IntegerField(verbose_name='Balcony type', choices=BALCONY_TYPES, null=True, blank=False)
    description = models.TextField(verbose_name='Description', null=True, blank=True)

    def __str__(self):
        return f'{self.realestate.plot.address.city}, {self.realestate.plot.address.street}' \
               f' {self.realestate.plot.address.street_number}/{self.apartment_number}'

    class Meta:
        verbose_name = 'Flat'


class Garage(models.Model):
    UNDERGROUND_GARAGE = 0
    EXTERNAL_PARKING_SPACE = 1
    DETACHED_GARAGE = 2
    ATTACHED_T0_THE_BUILDING = 3

    GARAGE_TYPES = (
        (UNDERGROUND_GARAGE, 'Underground'),
        (EXTERNAL_PARKING_SPACE, 'External space'),
        (DETACHED_GARAGE, 'Detached'),
        (ATTACHED_T0_THE_BUILDING, 'Attached')

    )

    realestate = models.ForeignKey(Realestate, on_delete=models.CASCADE, verbose_name='Realestate')
    type = models.IntegerField(verbose_name='Garage type', choices=GARAGE_TYPES)
    parking_number = models.PositiveSmallIntegerField(verbose_name='Parking space number')
    description = models.TextField(verbose_name='Description', null=True, blank=True)

    def __str__(self):
        return f'{self.get_type_display()}, ({self.realestate.plot.address.city}, ' \
               f'{self.realestate.plot.address.street} {self.realestate.plot.address.street_number}, ' \
               f'space number: {self.parking_number})'

    class Meta:
        verbose_name = 'Garage'


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
    limit = Q(app_label='realestates', model='plot') | Q(app_label='realestates', model='base') | \
        Q(app_label='realestates', model='flat') | Q(app_label='realestates', model='garage')  # wybór limitów
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to=limit)  # okreslenie limitu opcji
    object_id = GfkLookupField('content_type')  # lupka do wyboru obiektu
    content_object = GenericForeignKey('content_type', 'object_id')  # powiązuje content_type i object_id
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client', null=True, blank=True)

    def __str__(self):
        return f'{self.get_type_display()}, ({self.content_type})'

    class Meta:
        verbose_name = 'Offer'
