from django.test import TestCase

from attendance.models.Student import Student


class StudentTest(TestCase):

    def setUp(self):
        Student.objects.create(full_name="Rohan Sawant",
                               face_id="aae2f120-20d6-4fa7-b34c-f1dbe7aa09a9")
        Student.objects.create(full_name="Tanmay Sawant",
                               face_id="dae3f120-221d-42a7-b124c-f1dbe7aa09a9")

    def test_get_details(self):
        student_rohan = Student.objects.get(full_name="Rohan Sawant")
        student_tanmay = Student.objects.get(full_name="Tanmay Sawant")
        self.assertEqual(
            student_rohan.get_details(),
            "Rohan Sawant aae2f120-20d6-4fa7-b34c-f1dbe7aa09a9")
        self.assertEqual(
            student_tanmay.get_details(),
            "Tanmay Sawant dae3f120-221d-42a7-b124c-f1dbe7aa09a9")
