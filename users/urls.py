from django.conf.urls import url, include
# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

users_router = DefaultRouter()
users_router.register(r'users', UserViewSet)