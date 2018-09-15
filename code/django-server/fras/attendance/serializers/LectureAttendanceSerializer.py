from rest_framework import serializers

from attendance.models.LectureAttendance import LectureAttendance
from attendance.serializers.WorkingDaySerializer import WorkingDaySerializer


class LectureAttendanceSerializer(serializers.ModelSerializer):
    lecture_attendance_list = WorkingDaySerializer(many=True, read_only=True)

    class Meta:
        model = LectureAttendance
        fields = '__all__'
