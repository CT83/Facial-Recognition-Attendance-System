from rest_framework.response import Response
from rest_framework.views import APIView

from attendance.models.Student import Student
from attendance.serializers.StudentSerializer import StudentSerializer


class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def put(self, request):
        pass
