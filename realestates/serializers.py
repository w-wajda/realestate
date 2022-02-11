from django.contrib.auth.models import User

from rest_framework import serializers

from realestates.models import (
    Client,
    Address,
    Plot,
    Realestate,
    Flat,
    Garage,
    Offer
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'email', 'mobile_number']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'street_number', 'zip_code', 'city']


class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ['type', 'total_area', 'address', 'description']


class RealestateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestate
        fields = ['plot', 'type', 'area', 'number_floors', 'year_built', 'description']


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ['realestate', 'area', 'floor_number', 'apartment_number', 'rooms', 'kitchen_type', 'bathroom',
                  'balcony_type', 'description']


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = ['realestate', 'type', 'parking_number', 'description']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['type', 'price', 'description', 'content_type', 'object_id', 'client']








