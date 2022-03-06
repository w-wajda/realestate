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
    list_display = ('address', )
    list_filter = ('city', )
    search_fields = ['city', 'street']
    fieldsets = (
        ('Address data', {
            'fields': (('street', 'street_number'), ('zip_code', 'city')),
        }),
    )

    @admin.display(description='Address')
    def address(self, obj):
        return "%s, %s %s" % (obj.city, obj.street, obj.street_number)


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
    list_display = ('address', 'type_plot', 'total_area_plot')
    list_filter = ('address__city', 'type_plot')
    search_fields = ['address__city', 'type_plot']
    fieldsets = (
        ('Basic information', {
            'fields': (('address', ), ('type_plot', 'total_area_plot'))
        }),
    )


@admin.register(Realestate)
class RealestateAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('type_realestate', 'plot', 'year_built')
    list_filter = ('type_realestate', )
    fieldsets = (
        ('Basic information', {
            'fields': (
                ('plot', ),
                ('type_realestate', 'number_floors'),
                ('year_built',)
            )
        }),
    )


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('realestate_type', 'realestate_address', 'area', 'rooms')
    list_filter = ('rooms', 'kitchen_type', 'balcony_type')
    search_fields = ['realestate__plot']

    fieldsets = (
        ('Basic information', {
            'fields': (
                ('realestate',),
                ('area', 'floor_number', 'rooms'),
                ('apartment_number', )
            )
        }),
        ('Apartment details', {
            'fields': (
                ('kitchen_type', 'balcony_type'),
                ('bathroom', )
            )
        }),
    )

    @admin.display(description='Realestate type')
    def realestate_type(self, obj):
        return "%s" % (obj.realestate.get_type_realestate_display(), )

    @admin.display(description='Flat address')
    def realestate_address(self, obj):
        return "%s, %s %s" % (obj.realestate.plot.address.city, obj.realestate.plot.address.street,
                              obj.realestate.plot.address.street_number)


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('type_garage', 'garage_address', 'parking_number')
    list_filter = ('type_garage', )
    search_fields = ['type_garage']
    fieldsets = (
        ('Basic information', {
            'fields': (
                ('realestate', ),
                ('type_garage', 'parking_number'),
            )
        }),
    )

    @admin.display(description='Garage address')
    def garage_address(self, obj):
        return "%s, %s %s" % (obj.realestate.plot.address.city, obj.realestate.plot.address.street,
                              obj.realestate.plot.address.street_number)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('type_offer', 'content_type', 'object_id', 'price', 'client')
    list_filter = ('type_offer', 'content_type')

    fieldsets = (
        ('Basic information', {
            'fields': (
                ('type_offer', 'content_type'),
                ('object_id', 'price'),
            )
        }),
        ('Additional information', {
            'fields': (
                ('description',),
                ('client', )
            )
        })
    )


