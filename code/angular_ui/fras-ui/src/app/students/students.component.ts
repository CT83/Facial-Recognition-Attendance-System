import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs';
import {DataService} from '../services/data.service';


@Component({
  selector: 'app-students',
  templateUrl: './students.component.html',
  styleUrls: ['./students.component.scss']
})
export class StudentsComponent implements OnInit {

  students$: Object;

  constructor(private data: DataService) {
  }

  ngOnInit() {
    this.data.getStudents().subscribe(
      data => this.students$ = data
    );
  }

}
