from rest_framework import serializers

from attendance.models.FaceId import FaceId


class FaceIdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FaceId
        fields = '__all__'
