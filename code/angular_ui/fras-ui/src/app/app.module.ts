import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { StudentsComponent } from './students/students.component';
import { DetailsComponent } from './details/details.component';
import { AttendanceTableComponent } from './attendance-table/attendance-table.component';

import { MatTableModule, MatButtonModule } from '@angular/material'
import { AttendanceService } from './services/attendance.service';
import { WorkingDayDetailsComponent } from './working-day-details/working-day-details.component';
import { LectureAttendanceDetailsComponent } from './lecture-attendance-details/lecture-attendance-details.component';



@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    StudentsComponent,
    DetailsComponent,
    AttendanceTableComponent,
    WorkingDayDetailsComponent,
    LectureAttendanceDetailsComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatTableModule,
    MatButtonModule,
  ],
  providers: [AttendanceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
