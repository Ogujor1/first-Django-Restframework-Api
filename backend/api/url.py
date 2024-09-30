from django.urls import path
from .views import home, post
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', home),
    path('api/', post),
    path('api/auth/', obtain_auth_token),
]
 