import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { WorkingDaysData } from '../models/working_days.model';

@Injectable({
  providedIn: 'root'
})
export class AttendanceService {
  url: string;

  constructor(private http: HttpClient) {
    // this.url = "https://fras-1.herokuapp.com/"
    this.url = "http://localhost:8000/"
  }

  getWorkingDays(): Observable<WorkingDaysData[]> {
    return this.http.get<WorkingDaysData[]>(this.url + 'working-days/');
  }

}
