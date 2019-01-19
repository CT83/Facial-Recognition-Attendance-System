import datetime

from django.db import models

from attendance.models.Student import Student


class LectureAttendance(models.Model):
    working_day = models.ForeignKey('attendance.WorkingDay',
                                    related_name="lecture_attendances",
                                    on_delete=models.CASCADE)
    lecture_name = models.CharField(max_length=100)
    start = models.DateField(default=datetime.datetime.now())
    end = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return self.lecture_name + " - " + str(self.working_day)

    def get_present_students(self):
        present_students = set()
        from attendance.models.CapturedFrame import CapturedFrame
        captured_frames = CapturedFrame.objects.filter(lecture_attendance=self)
        students_in_frames = [student for captured_frame in captured_frames for student in
                              captured_frame.students.all()]

        for student in students_in_frames:
            if students_in_frames.count(student) > 0:
                present_students.add(student)
        return present_students

    def get_no_absent_students(self):
        present = self.get_present_students()
        absent_count = len(Student.objects.all()) - len(present)
        return absent_count

    def get_absent_students(self):
        absent_students = []
        for student in Student.objects.all():
            if student not in self.get_present_students():
                absent_students.append(student)
        return absent_students
