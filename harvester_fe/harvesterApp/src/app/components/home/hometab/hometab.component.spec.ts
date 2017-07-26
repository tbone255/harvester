import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HometabComponent } from './hometab.component';

describe('HometabComponent', () => {
  let component: HometabComponent;
  let fixture: ComponentFixture<HometabComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HometabComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HometabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
