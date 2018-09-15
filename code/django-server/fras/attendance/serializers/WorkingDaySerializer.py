from rest_framework import serializers

from attendance.models.WorkingDay import WorkingDay
from attendance.serializers.LectureAttendanceSerializer import LectureAttendanceSerializer


class WorkingDaySerializer(serializers.HyperlinkedModelSerializer):
    lecture_attendances = LectureAttendanceSerializer(many=True)

    class Meta:
        model = WorkingDay
        fields = '__all__'

    def create(self, validated_data):
        date = validated_data.pop('date')
        working_day = WorkingDay(date=date)
        working_day.save()
        return working_day
