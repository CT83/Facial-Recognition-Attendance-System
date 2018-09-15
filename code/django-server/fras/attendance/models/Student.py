from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True,
                             verbose_name="Identification Number")
    full_name = models.CharField(max_length=100)
    face_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.full_name

    def get_details(self):
        return self.full_name + " " + self.face_id
