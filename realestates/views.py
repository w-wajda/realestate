from django.contrib.auth.models import User

from rest_framework import viewsets

from realestates.serializers import (
    UserSerializer,
    ClientSerializer,
    AddressSerializer,
    PlotSerializer,
    PlotUpdateSerializer,
    RealestateSerializer,
    RealestateUpdateSerializer,
    FlatSerializer,
    FlatUpdateSerializer,
    GarageSerializer,
    OfferSerializer,
    OfferUpdateSerializer
)

from realestates.models import (
    Client,
    Address,
    Plot,
    Realestate,
    Flat,
    Garage,
    Offer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PlotViewSet(viewsets.ModelViewSet):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer

    def get_serializer_class(self):  # wybór odpowiedniego serializera dla update, dla pozostałych standardowy
        if self.action == 'update':
            return PlotUpdateSerializer
        else:
            return super().get_serializer_class()


class RealestateViewSet(viewsets.ModelViewSet):
    queryset = Realestate.objects.all()
    serializer_class = RealestateSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return RealestateUpdateSerializer
        else:
            return super().get_serializer_class()


class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return FlatUpdateSerializer
        else:
            return super().get_serializer_class()


class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return OfferUpdateSerializer
        else:
            return super().get_serializer_class()








