# Register your models here.
from django.contrib import admin

from attendance.models.LectureAttendance import LectureAttendance
from attendance.models.Student import Student
from attendance.models.WorkingDay import WorkingDay

admin.site.register(WorkingDay)
admin.site.register(LectureAttendance)
admin.site.register(Student)
