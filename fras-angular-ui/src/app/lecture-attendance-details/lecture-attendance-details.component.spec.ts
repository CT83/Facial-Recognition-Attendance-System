import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LectureAttendanceDetailsComponent } from './lecture-attendance-details.component';

describe('LectureAttendanceDetailsComponent', () => {
  let component: LectureAttendanceDetailsComponent;
  let fixture: ComponentFixture<LectureAttendanceDetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LectureAttendanceDetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LectureAttendanceDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
