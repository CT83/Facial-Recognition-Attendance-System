from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from attendance.views.CapturedFrameAPI import CapturedFrameAPI
from attendance.views.LectureAttendanceAPI import LectureAttendanceAPI
from attendance.views.StudentList import StudentList
from attendance.views.WorkingDayAPI import WorkingDayAPI

router = DefaultRouter()
router.register(r'students', StudentList, base_name="student")
router.register(r'working-days', WorkingDayAPI, base_name="working-day")
router.register(r'lecture-attendances', LectureAttendanceAPI,
                base_name="lecture-attendances")
router.register(r'captured-frame', CapturedFrameAPI, base_name="captured-frame")

urlpatterns = [
    url(r'^', include(router.urls)),
]
