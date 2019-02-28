import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  url: string;

  constructor(private http: HttpClient) {
    // this.url = 'https://fras-1.herokuapp.com/'
    this.url = 'http://localhost:8000/'
  }

  getStudents() {
    return this.http.get(this.url + 'students/');
  }


  getStudentDetails(student_id) {
    return this.http.get(this.url + 'student-details/' + student_id);
  }


  getWorkingDayDetails(workingDay_id) {
    return this.http.get(this.url + 'working-days/' + workingDay_id);
  }


  getLectureAttendanceDetails(workingDay_id) {
    return this.http.get(this.url + 'lecture-attendances/' + workingDay_id);
  }


  getRecentCapturedFrames() {
    return this.http.get(this.url + 'recent-captured-frames/');
  }
}
