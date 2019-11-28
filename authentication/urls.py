from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication import views

AuthRouter = DefaultRouter()
AuthRouter.register(r'', views.AuthenticationViewSet, base_name='auth')

urlpatterns = [
    path(r'', include(AuthRouter.urls))
]
