from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from attendance.models.Student import Student
from attendance.serializers.StudentSerializer import StudentSerializer


class StudentDetails(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)
