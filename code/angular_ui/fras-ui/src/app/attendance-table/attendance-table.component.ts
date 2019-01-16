import { Component, OnInit } from '@angular/core';
import { DataSource } from '@angular/cdk/collections';
import { WorkingDaysData } from '../models/working_days.model';
import { Observable } from 'rxjs';
import { AttendanceService } from '../services/attendance.service';

@Component({
  selector: 'app-attendance-table',
  templateUrl: './attendance-table.component.html',
  styleUrls: ['./attendance-table.component.scss']
})
export class AttendanceTableComponent implements OnInit {

  dataSource = new WorkingDaysDataSource(this.workingDaysService);
  displayedColumns = ['date', 'present_students'];

  constructor(private workingDaysService: AttendanceService) { }

  ngOnInit() {

  }

}

export class WorkingDaysDataSource extends DataSource<any>{

  constructor(private workingDaysService: AttendanceService) {
    super();
  }


  connect(): Observable<WorkingDaysData[]> {
    return this.workingDaysService.getWorkingDays();
  }

  disconnect() { }
}
