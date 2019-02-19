import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-working-day-details',
  templateUrl: './working-day-details.component.html',
  styleUrls: ['./working-day-details.component.scss']
})
export class WorkingDayDetailsComponent implements OnInit {

  $working_day: any;

  constructor(private route: ActivatedRoute, private data: DataService) {
    this.route.params.subscribe(params => this.$working_day = params.id);
  }

  ngOnInit() {
    this.data.getWorkingDayDetails(this.$working_day).subscribe(
      data => this.$working_day = data
    );
  }
}

