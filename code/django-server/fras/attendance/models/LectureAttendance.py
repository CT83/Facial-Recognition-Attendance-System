from django.db import models

from attendance.models.CapturedFrame import CapturedFrame
from attendance.models.WorkingDay import WorkingDay


class LectureAttendance(models.Model):
    working_day = models.ForeignKey(WorkingDay,
                                    related_name="lecture_attendances",
                                    on_delete=models.CASCADE)
    lecture_name = models.CharField(max_length=100)

    # TODO Update this to one to many relation
    captured_frames = models.ManyToManyField(CapturedFrame, blank=True)

    def get_present_students(self):
        present_students = set()
        students_in_frames = [student for captured_frame in self.captured_frames.all() for student in
                              captured_frame.students.all()]

        for student in students_in_frames:
            if students_in_frames.count(student) > 5:
                present_students.add(student)
        print(present_students)
        return present_students
