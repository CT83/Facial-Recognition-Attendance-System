import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AttendanceTableComponent } from './attendance-table.component';

describe('AttendanceTableComponent', () => {
  let component: AttendanceTableComponent;
  let fixture: ComponentFixture<AttendanceTableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AttendanceTableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AttendanceTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
