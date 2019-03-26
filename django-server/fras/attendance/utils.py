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
        student = Student(id=1, full_name='Rohan Sawant', face_id='9ee44c8c-920d-41cd-a1e0-95e9c53e649e')
        student.save()

        student = Student(id=2, full_name='Tanmay Sawant', face_id='85e9211d-6e2a-4a0e-9dba-917311393e2e')
        student.save()

        student = Student(id=3, full_name='Anirudh Iyer', face_id='2274d070-127c-4472-bc48-9df549417c19')
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

