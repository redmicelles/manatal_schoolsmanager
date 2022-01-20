from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, StudentViewSet, SchoolStudentViewSet, index

#create router object and register routes
router = routers.SimpleRouter()
router.register('schools', SchoolViewSet)
router.register('students', StudentViewSet)

#Created Nested Routes
domains_router = routers.NestedSimpleRouter(router, 'schools', lookup='school')
domains_router.register('students', SchoolStudentViewSet, basename='school-students')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(domains_router.urls)),
]