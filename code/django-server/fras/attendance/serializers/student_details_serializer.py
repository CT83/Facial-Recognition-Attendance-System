from rest_framework import serializers

from attendance.models.Student import Student


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('full_name', 'face_id', 'id', 'total_present_days')

    full_name = serializers.CharField()
    face_id = serializers.CharField()
    total_present_days = serializers.SerializerMethodField()
    total_absent_days = serializers.SerializerMethodField()

    def get_total_present_days(self, obj):
        return 100
