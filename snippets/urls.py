from django.conf.urls import url, include
# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewSet

snippets_router = DefaultRouter()
snippets_router.register(r'snippets', SnippetViewSet)