from rest_framework import viewsets

from attendance.models.CapturedFrame import CapturedFrame
from attendance.serializers.CapturedFrameSerializer import CapturedFrameSerializer


class RecentCapturedFramesView(viewsets.ModelViewSet):
    queryset = CapturedFrame.objects.all().order_by('-id')[:20]
    serializer_class = CapturedFrameSerializer
