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
        fields = ['id', 'name', 'surname', 'email', 'mobile_number']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'street_number', 'zip_code', 'city']


class AddressUpdateSerializer(serializers.ModelSerializer):  # dodany validators, ze względu na unique in model
    class Meta:
        model = Address
        fields = ['id', 'street', 'street_number', 'zip_code', 'city']
        validators = []


class PlotSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)  # OneToOne

    class Meta:
        model = Plot
        fields = ['id', 'type_plot', 'total_area_plot', 'address']

    def create(self, validated_data):
        address = validated_data.pop('address')

        if address:
            address = Address.objects.create(**address)

        plot = Plot.objects.create(address=address, **validated_data)
        return plot


class PlotUpdateSerializer(serializers.ModelSerializer):
    address = AddressUpdateSerializer(many=False)  # OneToOne

    class Meta:
        model = Plot
        fields = ['id', 'type_plot', 'total_area_plot', 'address']

    def update(self, instance: Plot, validated_data):
        instance.type_plot = validated_data.get('type_plot', instance.type_plot)  # zwraca nowy "type", inaczej ten sam instance.type
        instance.total_area_plot = validated_data.get('total_area_plot', instance.total_area_plot)

        if 'address' in validated_data:
            address = validated_data.get('address')
            address, created = Address.objects.get_or_create(**address)

            if created:
                instance.address.delete()

            instance.address = address

        instance.save()
        return instance


class ShortPlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ['id', 'type_plot', 'total_area_plot', 'address']


class ShortPlotUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ['id', 'type_plot', 'total_area_plot', 'address']
        extra_kwargs = {
            'address': {'validators': []},
        }


class RealestateSerializer(serializers.ModelSerializer):
    plot = ShortPlotSerializer(many=False)

    class Meta:
        model = Realestate
        fields = ['id', 'plot', 'type_realestate', 'number_floors', 'year_built']

    def create(self, validated_data):
        plot = validated_data.pop('plot')

        if plot:
            plot = Plot.objects.create(**plot)

        realestate = Realestate.objects.create(plot=plot, **validated_data)
        return realestate


class RealestateUpdateSerializer(serializers.ModelSerializer):
    plot = ShortPlotUpdateSerializer(many=False)

    class Meta:
        model = Realestate
        fields = ['id', 'plot', 'type_realestate', 'number_floors', 'year_built']

    def update(self, instance: Realestate, validated_data):
        instance.type_realestate = validated_data.get('type_realestate', instance.type_realestate)
        instance.number_floors = validated_data.get('number_floors', instance.number_floors)
        instance.year_built = validated_data.get('year_built', instance.year_built)

        if 'plot' in validated_data:
            plot = validated_data.get('plot')

            if instance.plot:
                instance.plot.type_plot = plot['type_plot']
                instance.plot.total_area_plot = plot['total_area_plot']
                instance.plot.address = plot['address']

                instance.plot.save()
            else:
                plot = Plot.objects.create(**plot)
                instance.plot = plot

        instance.save()
        return instance


class RealestateForFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestate
        fields = ['id', 'plot', 'type_realestate', 'number_floors', 'year_built']


class RealestateUpdateForFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestate
        fields = ['id', 'plot', 'type_realestate', 'number_floors', 'year_built']
        extra_kwargs = {
            'plot': {'validators': []},
        }


class FlatSerializer(serializers.ModelSerializer):
    realestate = RealestateForFlatSerializer(many=False)  # FK

    class Meta:
        model = Flat
        fields = ['id', 'realestate', 'area', 'floor_number', 'apartment_number', 'rooms', 'kitchen_type', 'bathroom',
                  'balcony_type']

    def create(self, validated_data):
        realestate = validated_data.pop('realestate')

        if realestate:
            realestate, created = Realestate.objects.get_or_create(**realestate)

        flat = Flat.objects.create(realestate=realestate, **validated_data)
        return flat


class FlatUpdateSerializer(serializers.ModelSerializer):
    realestate = RealestateUpdateForFlatSerializer(many=False)

    class Meta:
        model = Flat
        fields = ['id', 'realestate', 'area', 'floor_number', 'apartment_number', 'rooms', 'kitchen_type', 'bathroom',
                  'balcony_type']

    def update(self, instance: Flat, validated_data):
        instance.area = validated_data.get('area', instance.area)
        instance.floor_number = validated_data.get('floor_number', instance.floor_number)
        instance.apartment_number = validated_data.get('apartment_number', instance.apartment_number)
        instance.rooms = validated_data.get('rooms', instance.rooms)
        instance.kitchen_type = validated_data.get('kitchen_type', instance.kitchen_type)
        instance.bathroom = validated_data.get('bathroom', instance.bathroom)
        instance.balcony_type = validated_data.get('balcony_type', instance.balcony_type)

        if 'realestate' in validated_data:
            realestate = validated_data.get('realestate')

            if instance.realestate:
                instance.realestate.type_realestate = realestate['type_realestate']
                instance.realestate.number_floors = realestate['number_floors']
                instance.realestate.year_built = realestate['year_built']
                instance.realestate.plot = realestate['plot']

                instance.realestate.save()

            else:
                realestate = Realestate.objects.create(**realestate)
                instance.realestate = realestate

        instance.save()
        return instance


class RealestateForGarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestate
        fields = ['id', 'plot']
        extra_kwargs = {
            'plot': {'validators': []},
        }


class RealestateUpdateForGarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestate
        fields = ['id', 'plot', 'type_realestate']
        extra_kwargs = {
            'plot': {'validators': []},
        }


class GarageSerializer(serializers.ModelSerializer):
    realestate = RealestateForGarageSerializer(many=False)  # KF

    class Meta:
        model = Garage
        fields = ['id', 'realestate', 'type_garage', 'parking_number']

    def create(self, validated_data):
        realestate = validated_data.pop('realestate')

        if realestate:
            realestate, created = Realestate.objects.get_or_create(**realestate)

        garage = Garage.objects.create(realestate=realestate, **validated_data)
        return garage


class GarageUpdateSerializer(serializers.ModelSerializer):
    realestate = RealestateUpdateForGarageSerializer(many=False)

    class Meta:
        model = Garage
        fields = ['id', 'realestate', 'type_garage', 'parking_number']

    def update(self, instance: Garage, validated_data):
        instance.type_garage = validated_data.get('type_garage', instance.type_garage)
        instance.parking_number = validated_data.get('parking_number', instance.parking_number)

        if 'realestate' in validated_data:
            realestate = validated_data.get('realestate')
            realestate, created = Realestate.objects.get_or_create(**realestate)

            if created:
                instance.realestate.delete()

            instance.realestate = realestate

        instance.save()
        return instance


class ClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'surname', 'email', 'mobile_number']
        validators = []


class OfferSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False)

    class Meta:
        model = Offer
        fields = ['id', 'type', 'price', 'description', 'content_type', 'object_id', 'client']

    def create(self, validated_data):
        client = validated_data.pop('client')

        if client:
            client, created = Client.objects.get_or_create(**client)

        offer = Offer.objects.get_or_create(client=client, **validated_data)
        return offer


class OfferUpdateSerializer(serializers.ModelSerializer):
    client = ClientUpdateSerializer(many=False)

    class Meta:
        model = Offer
        fields = ['id', 'typer', 'price', 'description', 'content_type', 'object_id', 'client']

    def update(self, instance: Offer, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.content_type = validated_data.get('content_type', instance.content_type)
        instance.object_id = validated_data.get('object_id', instance.object_id)

        if "client" in validated_data:
            client = validated_data.get('client')
            client, created = Client.objects.get_or_create(**client)

            if created:
                instance.client.delete()

            instance.client = client

        instance.save()
        return instance











