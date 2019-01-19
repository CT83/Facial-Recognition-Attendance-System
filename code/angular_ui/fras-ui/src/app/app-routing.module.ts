import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { StudentsComponent } from './students/students.component';
import { DetailsComponent } from './details/details.component';
import { AttendanceTableComponent } from './attendance-table/attendance-table.component';
import { WorkingDayDetailsComponent } from './working-day-details/working-day-details.component';

const routes: Routes = [
  {
    path: '',
    component: StudentsComponent
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
    path: 'attendance-table',
    component: AttendanceTableComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
