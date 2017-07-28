import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddNutritionComponent } from './add-nutrition.component';

describe('AddNutritionComponent', () => {
  let component: AddNutritionComponent;
  let fixture: ComponentFixture<AddNutritionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddNutritionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddNutritionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
