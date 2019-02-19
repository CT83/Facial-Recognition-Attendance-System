from rest_framework import serializers

from attendance.models.Student import Student


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('full_name', 'face_id', 'id', 'total_present_days', 'total_absent_days')

    full_name = serializers.CharField()
    face_id = serializers.CharField()
    total_present_days = serializers.SerializerMethodField()
    total_absent_days = serializers.SerializerMethodField()

    @staticmethod
    def get_total_present_days(obj):
        if obj.get_present_days():
            return len(obj.get_present_days())
        else:
            return 0

    @staticmethod
    def get_total_absent_days(obj):
        if obj.get_absent_days():
            return len(obj.get_absent_days())
        else:
            return 0
