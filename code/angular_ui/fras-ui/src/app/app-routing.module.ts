import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { StudentsComponent } from './students/students.component';
import { DetailsComponent } from './details/details.component';
import { AttendanceTableComponent } from './attendance-table/attendance-table.component';
import { WorkingDayDetailsComponent } from './working-day-details/working-day-details.component';
import { LectureAttendanceDetailsComponent } from './lecture-attendance-details/lecture-attendance-details.component';
import { RecentCapturedFramesComponent } from './recent-captured-frames/recent-captured-frames.component';

const routes: Routes = [
  {
    path: '',
    component: StudentsComponent
  },
  {
    path: 'recent-captured-frames',
    component: RecentCapturedFramesComponent
  },
  {
    path: 'details/:id',
    component: DetailsComponent
  },
  {
    path: 'working-day-details/:id',
    component: WorkingDayDetailsComponent
  },
  {
    path: 'lecture-attendance-details/:id',
    component: LectureAttendanceDetailsComponent
  },
  {
    path: 'attendance-table',
    component: AttendanceTableComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
