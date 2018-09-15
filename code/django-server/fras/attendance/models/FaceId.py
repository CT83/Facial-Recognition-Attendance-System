from django.db import models

from attendance.models.CapturedFrame import CapturedFrame


class FaceId(models.Model):
    captured_frame = models.ForeignKey('attendance.CapturedFrame',
                                       related_name="face_ids",
                                       on_delete=models.CASCADE)
    face_id = models.TextField()

    def __str__(self):
        return str(self.face_id)
