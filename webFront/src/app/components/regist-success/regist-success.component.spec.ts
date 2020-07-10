import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistSuccessComponent } from './regist-success.component';

describe('RegistSuccessComponent', () => {
  let component: RegistSuccessComponent;
  let fixture: ComponentFixture<RegistSuccessComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RegistSuccessComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistSuccessComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
