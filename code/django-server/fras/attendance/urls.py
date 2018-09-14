from django.urls import path

from attendance.views.CapturedFrameAPI import CapturedFrameAPI
from attendance.views.LectureAttendanceAPI import LectureAttendanceAPI
from attendance.views.StudentList import StudentList
from attendance.views.WorkingDayAPI import WorkingDayAPI

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('working-day/', WorkingDayAPI.as_view()),
    path('lecture-attendance/', LectureAttendanceAPI.as_view()),
    path('captured-frame/', CapturedFrameAPI.as_view()),
]
