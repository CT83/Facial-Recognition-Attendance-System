from django.db import models

from attendance.models.LectureAttendance import LectureAttendance


class CapturedFrame(models.Model):
    lecture_attendance = models.ForeignKey(LectureAttendance,
                                           related_name="captured_frames",
                                           on_delete=models.CASCADE)
    captured_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.captured_at)
