import { TestBed } from '@angular/core/testing';

import { AttendanceService } from './attendance.service';

describe('AttendanceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: AttendanceService = TestBed.get(AttendanceService);
    expect(service).toBeTruthy();
  });
});
