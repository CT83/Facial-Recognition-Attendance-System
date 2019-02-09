from datetime import date, timedelta

from attendance.models.LectureAttendance import LectureAttendance


def get_or_create_current_frame(date_time):
    p, created = LectureAttendance.objects.get_or_create(
        first_name='John',
        last_name='Lennon',
        defaults={'birthday': date(1940, 10, 9)},
    )


def convert_str_to_date(string):
    from datetime import datetime
    datetime.strptime(string, "%Y-%m-%d %H:%M:%S.%f")


def create_database():
    from attendance.models.Student import Student
    from attendance.models.WorkingDay import WorkingDay

    create_students = True
    create_working_days = True
    create_lecture_attendances = True

    if create_students:
        student = Student(full_name='Rohan Sawant', face_id='f0b07f85-3d65-4ff4-a1f9-41d1d11edb35')
        student.save()

        student = Student(full_name='Tanmay Sawant', face_id='e376f233-70b3-4b70-a30e-44b7990192bd')
        student.save()

        student = Student(full_name='Anirudh Iyer', face_id='301a333c-2bcf-45b1-b847-fe9191f2ecaa')
        student.save()

    if create_working_days:
        working_day = WorkingDay(date=date.today() + timedelta(1))
        working_day.save()

        working_day = WorkingDay(date=date.today())
        working_day.save()

        working_day = WorkingDay(date=date.today())
        working_day.save()

        working_day = WorkingDay(date=date.today() - timedelta(1))
        working_day.save()

        working_day = WorkingDay(date=date.today() - timedelta(2))
        working_day.save()

        working_day = WorkingDay(date=date.today() - timedelta(3))
        working_day.save()
        working_day = WorkingDay(date=date.today() - timedelta(4))
        working_day.save()

        working_day = WorkingDay(date=date.today() - timedelta(5))
        working_day.save()

        working_day = WorkingDay(date=date.today() - timedelta(6))
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

    # TODO Complete this and test it later
