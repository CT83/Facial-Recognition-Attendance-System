from django.db import models

from attendance.models.Student import Student


class CapturedFrame(models.Model):
    captured_at = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(Student,
                                      verbose_name="Students in Image",
                                      blank=True)

    def __str__(self):
        return str(self.captured_at)
