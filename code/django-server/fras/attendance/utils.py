def convert_str_to_date(string):
    from datetime import datetime
    datetime.strptime(string, "%Y-%m-%d %H:%M:%S.%f")


def create_database():
    from attendance.models.Student import Student
    from attendance.models.WorkingDay import WorkingDay
    from attendance.models.LectureAttendance import LectureAttendance
    from datetime import date, timedelta

    create_students = True
    create_working_days = True
    create_lecture_attendances = True

    if create_students:
        student = Student(id=1, full_name='Rohan Sawant', face_id='1bf15e0f-3837-493a-8f72-aa3e5e98694f')
        student.save()

        student = Student(id=2, full_name='Tanmay Sawant', face_id='1d7d18cb-8e0b-498d-80c6-0d95c3d391e0')
        student.save()

        student = Student(id=3, full_name='Anirudh Iyer', face_id='08ef7629-f8d8-406e-b366-88df696517d8')
        student.save()

    if create_working_days:
        for i in range(30):
            working_day = WorkingDay(date=date.today() + timedelta(i))
            working_day.save()

        working_day = WorkingDay(date=date.today())
        working_day.save()

    if create_lecture_attendances:
        for working_day in WorkingDay.objects.all():
            LectureAttendance(working_day=working_day, lecture_name="Physics").save()
            LectureAttendance(working_day=working_day, lecture_name="English").save()
            LectureAttendance(working_day=working_day, lecture_name="Geography").save()
            LectureAttendance(working_day=working_day, lecture_name="Civics").save()
            LectureAttendance(working_day=working_day, lecture_name="Recess").save()
            LectureAttendance(working_day=working_day, lecture_name="Recess").save()
            LectureAttendance(working_day=working_day, lecture_name="History").save()
            LectureAttendance(working_day=working_day, lecture_name="Mathematics").save()
            LectureAttendance(working_day=working_day, lecture_name="Biology").save()

