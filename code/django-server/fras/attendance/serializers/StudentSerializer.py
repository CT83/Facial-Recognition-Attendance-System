from rest_framework import serializers

from attendance.models.Student import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
