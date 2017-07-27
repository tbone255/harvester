import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddDropdownComponent } from './add-dropdown.component';

describe('AddDropdownComponent', () => {
  let component: AddDropdownComponent;
  let fixture: ComponentFixture<AddDropdownComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddDropdownComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddDropdownComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
