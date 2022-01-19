from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, StudentViewSet

router = DefaultRouter()
router.register('schools', SchoolViewSet, basename=None)
router.register('students', StudentViewSet, basename=None)

urlpatterns = [
    path('', include(router.urls)),
]