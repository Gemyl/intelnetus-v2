import { TestBed } from '@angular/core/testing';

import { MetadataExtractionService } from './metadata-extraction.service';

describe('MetadataExtractionService', () => {
  let service: MetadataExtractionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MetadataExtractionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
