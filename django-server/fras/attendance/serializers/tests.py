from django.test import TestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from attendance.models.Student import Student
from attendance.serializers.StudentSerializer import StudentSerializer


class StudentSerializerTest(TestCase):

    def setUp(self):
        factory = APIRequestFactory()
        request = factory.get('/students')

        self.student_attributes = {"full_name": "Rohan Sawant",
                                   "face_id": "aae2f120-20d6-4fa7-b34c-f1dbe7aa09a9"}
        self.serializer_data = {"full_name": "Tanmay Sawant",
                                "face_id": "dae3f120-221d-42a7-b124c-f1dbe7aa09a9"}

        serializer_context = {
            'request': Request(request),
        }

        self.student = Student.objects.create(**self.student_attributes)
        self.serializer = StudentSerializer(instance=self.student, context=serializer_context)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        print(data)
        self.assertCountEqual(set(data.keys()), {'full_name', 'face_id'})

    def test_face_id_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['face_id'], self.student_attributes['face_id'])

    def test_full_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['full_name'], self.student_attributes['full_name'])
