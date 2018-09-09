from django.db import models

from rest_api.models.CapturedFrame import CapturedFrame


class LectureAttendance(models.Model):
    full_name = models.CharField(max_length=100)
    face_id = models.CharField(max_length=250, blank=True)
    captured_frames = models.ManyToManyField(CapturedFrame)

    def get_present_students(self):
        present_students = set()
        students_in_frames = [student for captured_frame in self.captured_frames.all() for student in
                              captured_frame.students.all()]

        for student in students_in_frames:
            if students_in_frames.count(student) > 5:
                present_students.add(student)
        print(present_students)
        return present_students
