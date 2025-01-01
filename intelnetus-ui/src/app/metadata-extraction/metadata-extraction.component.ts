import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { LoadMetadata } from './store/actions/metadata-extraction.action';
import { GetMetadataInsightsAction } from './store/actions/metadata-insights.actions';
import { AppState } from '../app.state';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { MetadataSearchFormComponent } from './components/metadata-search-form/metadata-search-form.component';
import { GetMetadataRequest, Metadata, Variants } from './models/metadata-extraction.model';
import { PaginatorState } from 'primeng/paginator';
import { DatePipe } from '@angular/common'; 
import * as XLSX from 'xlsx';

@Component({
  selector: 'app-metadata-extraction',
  templateUrl: './metadata-extraction.component.html',
  styles: "@import '../../theme-colors.scss';"
})
export class MetadataExtractionComponent implements OnInit {
  public data: Array<Metadata> = [];
  public searchCriteria: GetMetadataRequest;
  public variants: Variants;
  public loading: boolean = false;
  public total: number = 0;
  public noVariants: boolean = false;
  public forExport: boolean = false;
  public headers = {
    publicationDoi: "DOI",
    publicationTitle: "Title",
    publicationYear: "Year",
    publicationCitationsCount: "Citations Count",
    publicationKeywords: "Keywords",
    publicationFields: "Fields",
    authorFirstName: "Author First Name",
    authorLastName: "Author Last Name",
    authorFieldsOfStudy: "Fields Of Study",
    authorCitationsCount: "Author Citations Count",
    organizationName: "Organization Name",
    organizationType1: "Primary Type",
    organizationType2: "Secondary Type",
    organizationCity: "City",
    organizationCountry: "Country"
  }

  constructor(
    private store$: Store<AppState>,
    private _modalService: NgbModal,
    private _datePipe: DatePipe
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

        if(this.forExport && response.data.length > 0) {
          this.forExport = false;
          this.exportToExcel(response.data);
        
        } else if (!this.forExport) {
          this.data = response.data;
          this.total = response.total;
          this.variants = response.variants;
  
          this.noVariants = 
            response.variants.publicationsVariants.originals.length == 0 &&
            response.variants.authorsVariants.originals.length == 0 &&
            response.variants.organizationsVariants.originals.length == 0

          this.store$.dispatch(GetMetadataInsightsAction({
            keywords: this.searchCriteria.keywords,
            operators: this.searchCriteria.operators,
            startYear: this.searchCriteria.startYear,
            endYear: this.searchCriteria.endYear,
            fields: this.searchCriteria.fields
          }))
        }

        this.loading = false;
      });
  }

  handlePageChange(event: PaginatorState) {        
    this.loading = true;

    this.searchCriteria.pageSize = event.rows;
    this.searchCriteria.offset = event.first;
    this.store$.dispatch(LoadMetadata(this.searchCriteria));
  }

  handleFilterChange(event: string) {
    this.loading = true;

    this.searchCriteria.filterValue = event;
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
      
      if(response) {
        this.loading = true;
        
        this.searchCriteria.keywords = response.keywords;
        this.searchCriteria.operators = response.operators;
        this.searchCriteria.startYear = response.startYear;
        this.searchCriteria.endYear = response.endYear;
        this.searchCriteria.fields = response.fields;

        this.store$.dispatch(LoadMetadata(this.searchCriteria));
      }
    });
  }

  handleExportExcel() {
    this.forExport = true;
    const searchCriteriaExcel = {
      ...this.searchCriteria,
      ...{
        offset: 0,
        pageSize: this.total
      }
    };

    this.store$.dispatch(LoadMetadata(searchCriteriaExcel));
  }

  exportToExcel(data: any): void {
    const file = this.sortExportFileData(data);
    const fileName = `intelnetus_metadata_${this._datePipe.transform(new Date(), "yyyy_MM_dd_HH_mm_ss")}.xlsx`
    const workbook = XLSX.utils.book_new();
    const worksheet = XLSX.utils.aoa_to_sheet(file);
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Overall');
    XLSX.writeFile(workbook, fileName);
  }

  sortExportFileData(data: any[]) {
    let headers = Object.values(this.headers);
    let fileContent = [headers];

    for (let i = 0; i < data.length; i++) {
      let row = [];
      for (let headersKey in this.headers) {
        if (Object.prototype.hasOwnProperty.call(this.headers, headersKey)) {
          let dataKey = headersKey;
          row.push(data[i][dataKey]);
        }
      }
      fileContent.push(row);
    }

    return fileContent;
  }

  
}
