from rest_framework import serializers

from attendance.models.WorkingDay import WorkingDay


class WorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = '__all__'
