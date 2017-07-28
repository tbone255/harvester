import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEventLogComponent } from './add-event-log.component';

describe('AddEventLogComponent', () => {
  let component: AddEventLogComponent;
  let fixture: ComponentFixture<AddEventLogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddEventLogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddEventLogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
