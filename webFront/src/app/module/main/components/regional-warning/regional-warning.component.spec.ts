import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RegionalWarningComponent } from './regional-warning.component';

describe('RegionalWarningComponent', () => {
  let component: RegionalWarningComponent;
  let fixture: ComponentFixture<RegionalWarningComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RegionalWarningComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegionalWarningComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
