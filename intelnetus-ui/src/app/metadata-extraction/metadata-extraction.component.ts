import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { LoadMetadata } from './store/actions/metadata-extraction.action';
import { AppState } from '../app.state';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { MetadataSearchFormComponent } from './components/metadata-search-form/metadata-search-form.component';
import { GetMetadataRequest, Metadata, Variants } from './models/metadata-extraction.model';
import { PaginatorState } from 'primeng/paginator';

@Component({
  selector: 'app-metadata-extraction',
  templateUrl: './metadata-extraction.component.html',
  styleUrls: []
})
export class MetadataExtractionComponent implements OnInit {
  public data: Array<Metadata> = [];
  public searchCriteria: GetMetadataRequest;
  public variants: Variants;
  public loading: boolean = false;
  public total: number = 0;
  public noVariants: boolean = false;

  constructor(
    private store$: Store<AppState>,
    private _modalService: NgbModal
  ) {}

  ngOnInit(): void {
    this.searchCriteria = new GetMetadataRequest();
    this.variants = {
      publicationsVariants: {
        originals: [],
        duplicates: []
      },
      authorsVariants: {
        originals: [],
        duplicates: []
      },
      organizationsVariants: {
        originals: [],
        duplicates: []
      }
    };

    this.store$
      .select((store) => store.metadataState)
      .subscribe(response => {
        this.data = response.data;
        this.total = response.total;
        this.variants = response.variants;

        this.noVariants = 
          response.variants.publicationsVariants.originals.length == 0 &&
          response.variants.authorsVariants.originals.length == 0 &&
          response.variants.organizationsVariants.originals.length == 0

        this.loading = false;
      });
  }

  handlePageChange(event: PaginatorState) {
    this.searchCriteria.pageSize = event.rows;
    this.searchCriteria.offset = event.first;
        
    this.loading = true;
    this.store$.dispatch(LoadMetadata(this.searchCriteria));
  }

  handleFilterChange(event: string) {
    this.searchCriteria.filterValue = event;

    this.loading = true;
    this.store$.dispatch(LoadMetadata(this.searchCriteria));
  }

  handleVariantsSelection(event: string) {
    this.searchCriteria.exclude = event;

    if(this.searchCriteria.keywords) {
      this.loading = true;
      this.store$.dispatch(LoadMetadata(this.searchCriteria));
    }
  }

  openSearchForm() {
    let modalRef = this._modalService.open(MetadataSearchFormComponent, {
      backdrop: 'static',
      centered: true,
      size: 'xl'
    });

    modalRef.result.then(response => {
      this.loading = true;

      if(response) {
        this.searchCriteria.keywords = response.keywords;
        this.searchCriteria.operators = response.operators;
        this.searchCriteria.startYear = response.startYear;
        this.searchCriteria.endYear = response.endYear;
        this.searchCriteria.fields = response.fields;

        this.store$.dispatch(LoadMetadata(this.searchCriteria));
      }
    });
  }
  
}
