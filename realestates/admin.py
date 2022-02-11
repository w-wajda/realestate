from django.contrib import admin
from realestates.models import (
    Address,
    Client,
    Plot,
    Realestate,
    Flat,
    Garage,
    Offer
)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_filter = ('city', )
    search_fields = ['city', 'street']
    fieldsets = (
        ('Address data', {
            'fields': (('street', 'street_number'), ('zip_code', 'city')),
        }),
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('client_data_together', 'email', 'mobile_number')
    list_filter = ('name', 'surname',)
    search_fields = ['name', 'surname', 'email', 'mobile_number']
    fieldsets = (
        ('Client data', {
            'fields': (('name', 'surname'), )
        }),
        ('Contact details', {
            'fields': (('email', 'mobile_number'), )
        })
    )

    @admin.display(description='Name and Surname')
    def client_data_together(self, obj):
        return "%s %s" % (obj.name, obj.surname)


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'



@admin.register(Realestate)
class RealestateAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'

