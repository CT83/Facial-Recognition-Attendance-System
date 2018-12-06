import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) {
  }

  getStudents() {
    return this.http.get('http://localhost:8000/students/');
  }


  getStudentDetails(student_id) {
    return this.http.get('http://localhost:8000/student-details/' + student_id);
  }
}
