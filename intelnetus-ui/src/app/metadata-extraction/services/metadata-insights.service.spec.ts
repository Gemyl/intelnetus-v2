import { TestBed } from '@angular/core/testing';

import { MetadataInsightsService } from './metadata-insights.service';

describe('MetadataInsightsService', () => {
  let service: MetadataInsightsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MetadataInsightsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
