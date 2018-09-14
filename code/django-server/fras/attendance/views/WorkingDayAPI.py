from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from attendance.models.WorkingDay import WorkingDay
from attendance.serializers.WorkingDaySerializer import WorkingDaySerializer


class WorkingDayAPI(APIView):
    def get(self, request):
        working_days = WorkingDay.objects.all()
        serializer = WorkingDaySerializer(working_days, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = WorkingDaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
