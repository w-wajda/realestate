from django.contrib import admin
from realestates.models import Flat, House, Address


@admin.register
class FlatAdmin(admin.ModelAdmin):
    pass

admin.site.register(House)
admin.site.register(Address)


