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
