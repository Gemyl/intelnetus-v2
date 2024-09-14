import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MetadataSearchFormComponent } from './metadata-search-form.component';

describe('MetadataSearchFormComponent', () => {
  let component: MetadataSearchFormComponent;
  let fixture: ComponentFixture<MetadataSearchFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MetadataSearchFormComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MetadataSearchFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
