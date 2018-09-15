from rest_framework import viewsets

from attendance.models.FaceId import FaceId
from attendance.serializers.FaceIdSerializer import FaceIdSerializer


class FaceIdViewset(viewsets.ModelViewSet):
    queryset = FaceId.objects.all()
    serializer_class = FaceIdSerializer
