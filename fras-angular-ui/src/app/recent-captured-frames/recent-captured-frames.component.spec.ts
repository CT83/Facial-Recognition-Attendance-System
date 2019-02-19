import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RecentCapturedFramesComponent } from './recent-captured-frames.component';

describe('RecentCapturedFramesComponent', () => {
  let component: RecentCapturedFramesComponent;
  let fixture: ComponentFixture<RecentCapturedFramesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecentCapturedFramesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecentCapturedFramesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
