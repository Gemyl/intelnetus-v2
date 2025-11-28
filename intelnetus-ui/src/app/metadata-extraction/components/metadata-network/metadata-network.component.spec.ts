import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MetadataNetworkComponent } from './metadata-network.component';

describe('MetadataNetworkComponent', () => {
  let component: MetadataNetworkComponent;
  let fixture: ComponentFixture<MetadataNetworkComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MetadataNetworkComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MetadataNetworkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
