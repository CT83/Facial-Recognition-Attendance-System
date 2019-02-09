import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) {
  }

  getStudents() {
    return this.http.get('https://fras-1.herokuapp.com/students/');
  }


  getStudentDetails(student_id) {
    return this.http.get('https://fras-1.herokuapp.com/student-details/' + student_id);
  }


  getWorkingDayDetails(workingDay_id) {
    return this.http.get('https://fras-1.herokuapp.com/working-days/' + workingDay_id);
  }


  getLectureAttendanceDetails(workingDay_id) {
    return this.http.get('https://fras-1.herokuapp.com/lecture-attendances/' + workingDay_id);
  }
}
