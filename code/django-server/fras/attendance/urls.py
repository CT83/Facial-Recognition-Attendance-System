from django.urls import path

from attendance.views.StudentList import StudentList

urlpatterns = [
    path('students/', StudentList.as_view()),
]
