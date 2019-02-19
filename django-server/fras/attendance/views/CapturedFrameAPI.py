from rest_framework import viewsets

from attendance.models.CapturedFrame import CapturedFrame
from attendance.serializers.CapturedFrameSerializer import CapturedFrameSerializer


class CapturedFrameAPI(viewsets.ModelViewSet):
    queryset = CapturedFrame.objects.all()
    serializer_class = CapturedFrameSerializer
