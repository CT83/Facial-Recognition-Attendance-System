from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from attendance.views.CapturedFrameAPI import CapturedFrameAPI
from attendance.views.FaceIdViewset import FaceIdViewset
from attendance.views.LectureAttendanceAPI import LectureAttendanceAPI
from attendance.views.StudentDetails import StudentDetails
from attendance.views.StudentList import StudentList
from attendance.views.WorkingDayAPI import WorkingDayAPI
from attendance.views.time_face_id_view import TimeFaceIdView

router = DefaultRouter()
router.register('students', StudentList)
router.register('student-details', StudentDetails, 'StudentDetails')
router.register('working-days', WorkingDayAPI)
router.register('lecture-attendances', LectureAttendanceAPI)
router.register('captured-frame', CapturedFrameAPI)
router.register('face-id', FaceIdViewset)
# router.register('time-face-id', TimeFaceIdView, 'TimeFaceIdView')

urlpatterns = [
    url('time-face-id$', TimeFaceIdView.as_view(), name='time_face_id'),
    url('', include(router.urls)),
]
