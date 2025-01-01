import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MetadataChartsComponent } from './metadata-charts.component';

describe('MetadataChartsComponent', () => {
  let component: MetadataChartsComponent;
  let fixture: ComponentFixture<MetadataChartsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MetadataChartsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MetadataChartsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
