from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from attendance.models.LectureAttendance import LectureAttendance
from attendance.serializers.LectureAttendanceSerializer import LectureAttendanceSerializer


class LectureAttendanceAPI(APIView):
    def get(self, request):
        working_days = LectureAttendance.objects.all()
        serializer = LectureAttendanceSerializer(working_days, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = LectureAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
