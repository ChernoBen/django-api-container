from rest_framework.serializers import ModelSerializer
from points.models import Points


class PointSerializer(ModelSerializer):
    class Meta:
        model = Points
        fields = ['id','name','description']