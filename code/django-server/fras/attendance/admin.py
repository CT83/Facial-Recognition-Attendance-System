# Register your models here.
from django.contrib import admin

from attendance.models.CapturedFrame import CapturedFrame
from attendance.models.FaceId import FaceId
from attendance.models.LectureAttendance import LectureAttendance
from attendance.models.Student import Student
from attendance.models.WorkingDay import WorkingDay

admin.site.register(WorkingDay)
admin.site.register(LectureAttendance)
admin.site.register(CapturedFrame)
admin.site.register(Student)
admin.site.register(FaceId)
