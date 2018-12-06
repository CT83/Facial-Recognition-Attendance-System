from rest_framework import serializers

from attendance.models.Student import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('full_name', 'face_id', 'id')

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        face_id = validated_data.pop('face_id')
        student = Student(full_name=full_name, face_id=face_id)
        student.save()
        return student
