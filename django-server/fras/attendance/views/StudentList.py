from rest_framework import viewsets

from attendance.models.Student import Student
from attendance.serializers.StudentSerializer import StudentSerializer


class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
