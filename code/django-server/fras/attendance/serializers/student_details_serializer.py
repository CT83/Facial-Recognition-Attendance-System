from rest_framework import serializers


class StudentDetailsSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    face_id = serializers.CharField()
    total_present_days = serializers.SerializerMethodField('get_total_present_days')

    def get_total_present_days(self, obj):
        pass
