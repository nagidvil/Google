import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CriticalPatientsComponent } from './critical-patients.component';

describe('CriticalPatientsComponent', () => {
  let component: CriticalPatientsComponent;
  let fixture: ComponentFixture<CriticalPatientsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CriticalPatientsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CriticalPatientsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
