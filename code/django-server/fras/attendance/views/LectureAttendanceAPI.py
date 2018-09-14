from rest_framework import viewsets

from attendance.models.LectureAttendance import LectureAttendance
from attendance.serializers.LectureAttendanceSerializer import LectureAttendanceSerializer


class LectureAttendanceAPI(viewsets.ModelViewSet):
    queryset = LectureAttendance.objects.all()
    serializer_class = LectureAttendanceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `id` query parameter in the URL.
        """
        queryset = LectureAttendance.objects.all()
        id = self.request.query_params.get('id', None)
        print("Query Params", self.request.query_params)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset
