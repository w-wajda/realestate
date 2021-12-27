from django.contrib import admin
from realestates.models import (
    Address,
    Plot,
    Realestate,
    Flat,
    Garage,
    Offer
)

admin.site.register(Address)
admin.site.register(Plot)
admin.site.register(Realestate)
admin.site.register(Flat)
admin.site.register(Garage)
admin.site.register(Offer)
