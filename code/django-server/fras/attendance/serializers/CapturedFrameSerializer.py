from rest_framework import serializers

from attendance.models.CapturedFrame import CapturedFrame
from attendance.models.LectureAttendance import LectureAttendance


class CapturedFrameSerializer(serializers.ModelSerializer):
    working_day = serializers.PrimaryKeyRelatedField(source='workingday_set', many=True,
                                                     queryset=LectureAttendance.objects.all())

    class Meta:
        model = CapturedFrame
        fields = '__all__'
