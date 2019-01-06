from datetime import date

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from attendance.models.CapturedFrame import CapturedFrame
from attendance.models.LectureAttendance import LectureAttendance
from attendance.models.Student import Student
from attendance.models.WorkingDay import WorkingDay


class TimeFaceIdView(APIView):
    """
    Allow [time,[face_ids]] to be added to the database, the API will
    automatically add the face_ids in the proper location based on
    the current time
    """

    def post(self, request, format=None):
        lecture_number = request.data['lecture_number']
        face_ids = request.POST.getlist('face_ids')

        students = [Student.objects.filter(face_id=face_id).first() for face_id in face_ids]

        working_day = WorkingDay.objects.filter(date=date.today()).first()
        lecture_attendance = LectureAttendance.objects.filter(working_day=working_day).all()[int(lecture_number)]
        captured_frame = CapturedFrame(lecture_attendance=lecture_attendance, students=students)
        captured_frame.save()

        return Response(request.data, status=status.HTTP_201_CREATED)

    @classmethod
    def get_extra_actions(cls):
        return []
