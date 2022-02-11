from django.contrib import admin
from django.urls import (
    path,
    include
)

from rest_framework.authtoken.views import obtain_auth_token

from base import urls_api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls_api)),
    path('api-token-auth/', obtain_auth_token)
]



