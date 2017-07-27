import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddPlantComponent } from './add-plant.component';

describe('AddPlantComponent', () => {
  let component: AddPlantComponent;
  let fixture: ComponentFixture<AddPlantComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddPlantComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddPlantComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
