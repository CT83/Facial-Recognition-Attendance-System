from django.db import models

from attendance.models.LectureAttendance import LectureAttendance


class WorkingDay(models.Model):
    date = models.DateField(primary_key=True)
    lectures_attendances = models.ManyToManyField(LectureAttendance)
