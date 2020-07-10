import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GainWebInfoComponent } from './gain-web-info.component';

describe('GainWebInfoComponent', () => {
  let component: GainWebInfoComponent;
  let fixture: ComponentFixture<GainWebInfoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GainWebInfoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GainWebInfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
