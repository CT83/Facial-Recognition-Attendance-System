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
        fields = ('working_day', 'lecture_name', 'present_students', 'absent_students')

    present_students = serializers.SerializerMethodField()
    absent_students = serializers.SerializerMethodField()

    def create(self, validated_data):
        working_day = validated_data.pop('working_day')
        lecture_name = validated_data.pop('lecture_name')
        print(validated_data)
        lecture_attendance = LectureAttendance(working_day=working_day, lecture_name=lecture_name)
        lecture_attendance.save()
        return lecture_attendance

    @staticmethod
    def get_present_students(obj):
        if obj.get_present_students():
            students = obj.get_present_students()
            return len(students)
        else:
            return 0

    @staticmethod
    def get_absent_students(obj):
        if len(obj.get_absent_students()):
            return len(obj.get_absent_students())
        else:
            return 0
