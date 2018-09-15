from rest_framework import serializers

from attendance.models.LectureAttendance import LectureAttendance
from attendance.models.WorkingDay import WorkingDay
from attendance.serializers.LectureAttendanceSerializer import LectureAttendanceSerializer


class WorkingDaySerializer(serializers.ModelSerializer):
    lecture_attendances = LectureAttendanceSerializer(many=True)

    class Meta:
        model = WorkingDay
        fields = '__all__'

    def create(self, validated_data):
        print("Validated Data", validated_data)
        profile_data = validated_data.pop('lecture_attendances')
        working_day = WorkingDay.objects.create(**validated_data)
        LectureAttendance.objects.create(working_day=working_day, **profile_data)
        return working_day
