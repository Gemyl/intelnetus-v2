import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VariantsModalComponent } from './variants-modal.component';

describe('VariantsModalComponent', () => {
  let component: VariantsModalComponent;
  let fixture: ComponentFixture<VariantsModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VariantsModalComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(VariantsModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
