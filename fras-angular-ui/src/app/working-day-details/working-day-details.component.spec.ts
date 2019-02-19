import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkingDayDetailsComponent } from './working-day-details.component';

describe('WorkingDayDetailsComponent', () => {
  let component: WorkingDayDetailsComponent;
  let fixture: ComponentFixture<WorkingDayDetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkingDayDetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkingDayDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
