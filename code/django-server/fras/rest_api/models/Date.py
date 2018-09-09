from django.db import models

from rest_api.models.LectureAttendance import LectureAttendance


class Date(models.Model):
    date = models.DateField(primary_key=True)
    lectures_attendances = models.ManyToManyField(LectureAttendance)
