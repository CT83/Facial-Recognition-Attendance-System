from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from attendance.models.CapturedFrame import CapturedFrame
from attendance.serializers.CapturedFrameSerializer import CapturedFrameSerializer


class CapturedFrameAPI(APIView):
    def get(self, request):
        working_days = CapturedFrame.objects.all()
        serializer = CapturedFrameSerializer(working_days, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = CapturedFrameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
