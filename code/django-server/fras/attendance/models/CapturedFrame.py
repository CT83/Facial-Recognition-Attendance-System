from django.db import models

from attendance.models.Student import Student


class CapturedFrame(models.Model):
    lecture_attendance = models.ForeignKey('attendance.LectureAttendance',
                                           related_name="captured_frames",
                                           on_delete=models.CASCADE)
    captured_at = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(Student, null=True)
    image_link = models.URLField(blank=True)
