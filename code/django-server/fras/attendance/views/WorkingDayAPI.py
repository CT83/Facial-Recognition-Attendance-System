from rest_framework import viewsets

from attendance.models.WorkingDay import WorkingDay
from attendance.serializers.WorkingDaySerializer import WorkingDaySerializer


class WorkingDayAPI(viewsets.ModelViewSet):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer
