from django.db import models


class CapturedFrame(models.Model):
    lecture_attendance = models.ForeignKey('attendance.LectureAttendance',
                                           related_name="captured_frames",
                                           on_delete=models.CASCADE)
    captured_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.captured_at)
