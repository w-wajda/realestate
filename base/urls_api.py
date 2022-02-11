from django.urls import include, path
from rest_framework import routers
from realestates import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'addresses', views.AddressViewSet)
router.register(r'plots', views.PlotViewSet)
router.register(r'realestates', views.RealestateViewSet)
router.register(r'flats', views.FlatViewSet)
router.register(r'garages', views.GarageViewSet)
router.register(r'offers', views.OfferViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
