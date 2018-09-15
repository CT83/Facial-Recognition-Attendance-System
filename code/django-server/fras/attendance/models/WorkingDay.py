from django.db import models
from django.utils.translation import gettext as _

from attendance.models.LectureAttendance import LectureAttendance


class WorkingDay(models.Model):
    date = models.DateField(_("Date"))
    lecture_attendances = models.ManyToManyField(LectureAttendance,
                                                 related_name='lecture_attendance_list',
                                                 blank=True)
