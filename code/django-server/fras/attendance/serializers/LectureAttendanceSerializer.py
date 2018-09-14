from rest_framework import serializers

from attendance.models.LectureAttendance import LectureAttendance
from attendance.models.WorkingDay import WorkingDay


class LectureAttendanceSerializer(serializers.ModelSerializer):
    working_day = serializers.PrimaryKeyRelatedField(source='workingday_set', many=True,
                                                     queryset=WorkingDay.objects.all())

    class Meta:
        model = LectureAttendance
        fields = '__all__'
