from django.urls import path

from attendance.views.StudentList import StudentList
from attendance.views.WorkingDayAPI import WorkingDayAPI

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('working-day/', WorkingDayAPI.as_view()),
]
