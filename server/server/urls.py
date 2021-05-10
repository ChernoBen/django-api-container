from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from points.api.viewsets import PointViewSet
from attractions.api.viewsets import AttractionsViewSet


router = routers.DefaultRouter()
router.register(r'points',PointViewSet)
router.register(r'attractions',AttractionsViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
