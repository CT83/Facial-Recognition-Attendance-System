from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from attendance.views.CapturedFrameAPI import CapturedFrameAPI
from attendance.views.LectureAttendanceAPI import LectureAttendanceAPI
from attendance.views.StudentList import StudentList
from attendance.views.WorkingDayAPI import WorkingDayAPI

router = DefaultRouter()
router.register('students', StudentList)
router.register('working-days', WorkingDayAPI)
router.register('lecture-attendances', LectureAttendanceAPI)
router.register(r'captured-frame', CapturedFrameAPI)

urlpatterns = [
    url('', include(router.urls)),
]
