import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CustomWebinfoComponent } from './custom-webinfo.component';

describe('CustomWebinfoComponent', () => {
  let component: CustomWebinfoComponent;
  let fixture: ComponentFixture<CustomWebinfoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CustomWebinfoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CustomWebinfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
