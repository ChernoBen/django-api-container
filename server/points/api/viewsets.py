from rest_framework.viewsets import ModelViewSet
from points.models import Points
from .serializers import PointSerializer


class PointViewSet(ModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointSerializer