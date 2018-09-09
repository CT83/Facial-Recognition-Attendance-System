# Register your models here.
from django.contrib import admin

from rest_api.models.LectureAttendance import LectureAttendance
from rest_api.models.Student import Student
from rest_api.models.WorkingDay import WorkingDay

admin.site.register(WorkingDay)
admin.site.register(LectureAttendance)
admin.site.register(Student)
