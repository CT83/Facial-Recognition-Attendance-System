from django.db import models

from attendance.models.LectureAttendance import LectureAttendance


class WorkingDay(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=False)
    lectures_attendances = models.ManyToManyField(LectureAttendance, blank=True)
