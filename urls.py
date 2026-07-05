from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]