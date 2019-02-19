from rest_framework import serializers

from attendance.models.CapturedFrame import CapturedFrame


class CapturedFrameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CapturedFrame
        fields = '__all__'
