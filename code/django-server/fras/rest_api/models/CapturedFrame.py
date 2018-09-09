from django.db import models

from rest_api.models.Student import Student


class CapturedFrame(models.Model):
    captured_at = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(Student,
                                      verbose_name="Students in Image")
