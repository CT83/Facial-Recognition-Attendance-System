import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-lecture-attendance-details',
  templateUrl: './lecture-attendance-details.component.html',
  styleUrls: ['./lecture-attendance-details.component.scss']
})
export class LectureAttendanceDetailsComponent implements OnInit {

  $lecture_attendance: Object;

  constructor(private route: ActivatedRoute, private data: DataService) {
    this.route.params.subscribe(params => this.$lecture_attendance = params.id);
  }

  ngOnInit() {
    this.data.getWorkingDayDetails(this.$lecture_attendance).subscribe(
      data => this.$lecture_attendance = data
    );
  }
}