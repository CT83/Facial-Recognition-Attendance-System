from rest_framework import viewsets

from attendance.models.LectureAttendance import LectureAttendance
from attendance.serializers.LectureAttendanceSerializer import LectureAttendanceSerializer


class LectureAttendanceAPI(viewsets.ModelViewSet):
    queryset = LectureAttendance.objects.all()
    serializer_class = LectureAttendanceSerializer
