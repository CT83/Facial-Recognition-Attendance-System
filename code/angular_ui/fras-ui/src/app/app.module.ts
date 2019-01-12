import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {SidebarComponent} from './sidebar/sidebar.component';
import {StudentsComponent} from './students/students.component';
import { DetailsComponent } from './details/details.component';
import { AttendanceTableComponent } from './attendance-table/attendance-table.component';

import {MatTableModule} from '@angular/material'
import {AttendanceService} from './services/attendance.service';



@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    StudentsComponent,
    DetailsComponent,
    AttendanceTableComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatTableModule,
  ],
  providers: [AttendanceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
