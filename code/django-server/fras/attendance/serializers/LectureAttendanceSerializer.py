from rest_framework import serializers

from attendance.models.LectureAttendance import LectureAttendance


class LectureAttendanceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LectureAttendance
        fields = '__all__'
