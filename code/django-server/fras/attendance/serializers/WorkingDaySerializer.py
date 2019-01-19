from rest_framework import serializers

from attendance.models.WorkingDay import WorkingDay
from attendance.serializers.LectureAttendanceSerializer import LectureAttendanceSerializer
from attendance.serializers.StudentSerializer import StudentSerializer


class WorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = ('id', 'date', 'lecture_attendances', 'present_students', 'absent_students')

    lecture_attendances = LectureAttendanceSerializer(many=True)
    present_students = serializers.SerializerMethodField()
    absent_students = serializers.SerializerMethodField()

    def create(self, validated_data):
        date = validated_data.pop('date')
        working_day = WorkingDay(date=date)
        working_day.save()
        return working_day

    @staticmethod
    def get_present_students(obj):
        if obj.get_present_students():
            students = obj.get_present_students()
            serializer = StudentSerializer(students, many=True)
            # return serializer.data
            return len(students)

        else:
            return []

    @staticmethod
    def get_absent_students(obj):
        if obj.get_absent_students():
            return len(obj.get_absent_students())
        else:
            return 0
