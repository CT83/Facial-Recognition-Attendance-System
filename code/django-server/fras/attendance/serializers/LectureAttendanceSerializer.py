from rest_framework import serializers

from attendance.models.LectureAttendance import LectureAttendance
from attendance.models.WorkingDay import WorkingDay


class LectureAttendanceSerializer(serializers.ModelSerializer):
    working_day = serializers.SlugRelatedField(
        many=False,
        queryset=WorkingDay.objects.all(),
        slug_field='date'
    )

    class Meta:
        model = LectureAttendance
        fields = ('working_day', 'lecture_name')

    def create(self, validated_data):
        working_day = validated_data.pop('working_day')
        lecture_name = validated_data.pop('lecture_name')
        print(validated_data)
        lecture_attendance = LectureAttendance(working_day=working_day, lecture_name=lecture_name)
        lecture_attendance.save()
        return lecture_attendance
