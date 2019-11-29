from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication import views

AuthRouter = DefaultRouter()
AuthRouter.register(r'', views.AuthenticationViewSet, base_name='auth')
AuthRouter.register(r'users', views.ProfileViewSet, base_name='users')

urlpatterns = [
    path(r'', include(AuthRouter.urls))
]
