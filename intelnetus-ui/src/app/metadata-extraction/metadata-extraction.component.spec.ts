import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MetadataExtractionComponent } from './metadata-extraction.component';

describe('MetadataExtractionComponent', () => {
  let component: MetadataExtractionComponent;
  let fixture: ComponentFixture<MetadataExtractionComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MetadataExtractionComponent]
    });
    fixture = TestBed.createComponent(MetadataExtractionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
