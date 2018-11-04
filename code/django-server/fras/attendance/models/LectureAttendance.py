from django.db import models


class LectureAttendance(models.Model):
    working_day = models.ForeignKey('attendance.WorkingDay',
                                    related_name="lecture_attendances",
                                    on_delete=models.CASCADE)
    lecture_name = models.CharField(max_length=100)

    def __str__(self):
        return self.lecture_name + " - " + str(self.working_day)


def get_present_students(lecture_attendance):
    present_students = set()
    from attendance.models.CapturedFrame import CapturedFrame
    captured_frames = CapturedFrame.objects.filter(lecture_attendance=lecture_attendance)
    students_in_frames = [student for captured_frame in captured_frames for student in
                          captured_frame.students.all()]

    for student in students_in_frames:
        if students_in_frames.count(student) > 5:
            present_students.add(student)
    print(present_students)
    return present_students
