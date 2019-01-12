from django.db import models
from django.utils.translation import gettext as _

from attendance.models.LectureAttendance import LectureAttendance


class WorkingDay(models.Model):
    date = models.DateField(_("Date"))

    def __str__(self):
        return str(self.date)

    def get_present_students(self):
        lecture_attendances = LectureAttendance.objects.filter(working_day=self)

        present_students = []
        present_students_day = set()

        for lecture_attendance in lecture_attendances:
            present_students += lecture_attendance.get_present_students()

        for student in present_students:
            if present_students.count(student) > 0:
                present_students_day.add(student)
        return present_students_day

    def get_absent_students(self):
        pass
