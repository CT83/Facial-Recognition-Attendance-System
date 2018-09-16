import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from attendance.models.LectureAttendance import LectureAttendance
from attendance.models.Student import Student
from attendance.models.WorkingDay import WorkingDay


class StudentTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new student object.
        """
        student_attributes = {"full_name": "Rohan Sawant",
                              "face_id": "aae2f120-20d6-4fa7-b34c-f1dbe7aa09a"}
        response = self.client.post('/students/', student_attributes, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().full_name, 'Rohan Sawant')
        self.assertEqual(Student.objects.get().face_id, 'aae2f120-20d6-4fa7-b34c-f1dbe7aa09a')


class WorkingDayTests(APITestCase):
    def test_create_working_day(self):
        """
        Ensure we can create a new student object.
        """
        working_day_data = {"date": "2018-08-23", "lecture_attendances": []}
        response = self.client.post('/working-days/', working_day_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WorkingDay.objects.count(), 1)
        self.assertEqual(WorkingDay.objects.get().date, datetime.date(2018, 8, 23))


class LectureAttendanceTests(APITestCase):

    def setUp(self):
        working_day_data = {"date": "2018-08-15", "lecture_attendances": []}
        self.client.post('/working-days/', working_day_data, format='json')

    def test_create_lecture_attendace(self):
        """
        Ensure we can create a new student object.
        """
        lecture_attendance_date = {"working_day": "2018-08-15", "lecture_name": "Maths"}
        response = self.client.post('/lecture-attendances/', lecture_attendance_date, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LectureAttendance.objects.count(), 1)
        self.assertEqual(
            str(LectureAttendance.objects.get().working_day),
            '2018-08-15')
