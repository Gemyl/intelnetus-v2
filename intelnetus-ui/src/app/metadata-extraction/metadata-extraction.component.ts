import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { LoadMetadata } from './store/actions/metadata-extraction.action';
import { AppState } from '../app.state';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { MetadataSearchFormComponent } from './components/metadata-search-form/metadata-search-form.component';
import { GetMetadataRequest, Metadata } from './models/metadata-extraction.model';
import { TablePageEvent } from 'primeng/table';
import { PaginatorState } from 'primeng/paginator';

@Component({
  selector: 'app-metadata-extraction',
  templateUrl: './metadata-extraction.component.html',
  styleUrls: []
})
export class MetadataExtractionComponent implements OnInit {
  public data: Array<Metadata> = [];
  public loading: boolean = false;
  public pageSize: number = 10;
  public offset: number = 10;
  public total: number = 0;
  public searchCriteria: GetMetadataRequest;

  constructor(
    private store$: Store<AppState>,
    private _modalService: NgbModal
  ) {}

  ngOnInit(): void {
    this.store$
      .select((store) => store.metadataState)
      .subscribe(response => {
        this.data = response.data;
        this.total = response.total;
        this.loading = false;
      });
  }

  getPageState(event: PaginatorState) {
    this.pageSize = event.rows;
    this.offset = event.first;
    const request = {...this.searchCriteria, ...{pageSize: this.pageSize, offset: this.offset}};
        
    this.store$.dispatch(LoadMetadata(request));
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
        this.searchCriteria = response;
        response = {...response, ...{pageSize: this.pageSize, offset: this.offset}};

        this.store$.dispatch(LoadMetadata(response));
      }
    });
  }
  
}
