from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from attendance.utils import get_or_create_current_frame, convert_str_to_date


class TimeFaceIdView(APIView):
    """
    Allow [time,[face_ids]] to be added to the database, the API will
    automatically add the face_ids in the proper location based on
    the current time
    """

    def post(self, request, format=None):
        print(request.data)
        current_time = request.data['current_time']

        face_ids = request.data['face_ids']

        get_or_create_current_frame(convert_str_to_date(current_time))
        return Response(request.data, status=status.HTTP_201_CREATED)

    @classmethod
    def get_extra_actions(cls):
        return []
