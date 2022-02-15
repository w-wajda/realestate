from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

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
        fields = ['username', 'first_name', 'last_name', 'password', 'email']

        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True, 'validators': [UniqueValidator(queryset=User.objects.all())]}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'email', 'mobile_number']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'street_number', 'zip_code', 'city']


class PlotSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)  # OneToOne

    class Meta:
        model = Plot
        fields = ['type', 'total_area', 'address', 'description']

    def create(self, validated_data):
        address = validated_data.pop('address')

        if address:
            address = Address.objects.create(**address)

        plot = Plot.objects.create(address=address, **validated_data)
        return plot


class AddressUpdateSerializer(serializers.ModelSerializer):  # dodany validators, ze względu na unique in model
    class Meta:
        model = Address
        fields = ['street', 'street_number', 'zip_code', 'city']
        validators = []


class PlotUpdateSerializer(serializers.ModelSerializer):
    address = AddressUpdateSerializer(many=False)  # OneToOne

    class Meta:
        model = Plot
        fields = ['type', 'total_area', 'address', 'description']

    def update(self, instance: Plot, validated_data):
        instance.type = validated_data.get('type', instance.type)  # zwraca nowy "type", inaczej ten sam instance.type
        instance.total_area = validated_data.get('total_area', instance.total_area)
        instance.description = validated_data.get('description', instance.description)

        if 'address' in validated_data:
            address = validated_data.get('address')
            address, created = Address.objects.get_or_create(**address)

            if created:
                instance.address.delete()

            instance.address = address

        instance.save()
        return instance


class RealestateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestate
        fields = ['plot', 'type', 'number_floors', 'year_built', 'description']


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ['realestate', 'area', 'floor_number', 'apartment_number', 'rooms', 'kitchen_type', 'bathroom',
                  'balcony_type', 'description']


class ShortRealestateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestate
        fields = ['plot', 'type']
        extra_kwargs = {
            'plot': {'validators': []},
        }


class GarageSerializer(serializers.ModelSerializer):
    realestate = ShortRealestateSerializer(many=False)  # KF

    class Meta:
        model = Garage
        fields = ['realestate', 'type', 'parking_number', 'description']

    def create(self, validated_data):
        realestate = validated_data.pop('realestate')

        if realestate:
            realestate, created = Realestate.objects.get_or_create(**realestate)

        garage = Garage.objects.create(realestate=realestate, **validated_data)
        return garage


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['type', 'price', 'description', 'content_type', 'object_id', 'client']








