from django.db import models
from django.utils.translation import gettext as _

from attendance.models.LectureAttendance import LectureAttendance


class WorkingDay(models.Model):
    date = models.DateField(_("Date"), auto_now_add=True)
    lectures_attendances = models.ManyToManyField(LectureAttendance, blank=True)
