from django.urls import path, include
from .views import index
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, StudentViewSet,index

router = DefaultRouter()
router.register('schools', SchoolViewSet, basename=None)
router.register('students', StudentViewSet, basename=None)

urlpatterns = [
    path('', index),
    path('api/', include(router.urls)),
]