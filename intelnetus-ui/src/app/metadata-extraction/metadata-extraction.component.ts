import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { LoadMetadata } from './store/actions/metadata-extraction.action';
import { AppState } from '../app.state';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { MetadataSearchFormComponent } from './components/metadata-search-form/metadata-search-form.component';
import { Metadata } from './models/metadata-extraction.model';

@Component({
  selector: 'app-metadata-extraction',
  templateUrl: './metadata-extraction.component.html',
  styleUrls: []
})
export class MetadataExtractionComponent implements OnInit {
  public data: Array<Metadata> = [];
  public loading: boolean = false;

  constructor(
    private store$: Store<AppState>,
    private _modalService: NgbModal
  ) {}

  ngOnInit(): void {
    this.store$
      .select((store) => store.metadataState)
      .subscribe(response => {
        this.data = response.data;
        this.loading = false;
      });
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
        this.store$.dispatch(LoadMetadata(response));
      }
    });
  }
  
}
