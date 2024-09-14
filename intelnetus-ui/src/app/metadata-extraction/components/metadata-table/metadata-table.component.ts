import { Component, ViewChild, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { SortEvent } from 'primeng/api';
import { Table } from 'primeng/table';
import { Metadata } from '../../models/metadata-extraction.model';
import { PaginatorState } from 'primeng/paginator';

@Component({
  selector: 'app-metadata-table',
  templateUrl: './metadata-table.component.html',
  styleUrls: []
})
export class MetadataTableComponent implements OnInit {
  @ViewChild("dt") dataGrid: Table;
  @Output() onPageChange: EventEmitter<PaginatorState> = new EventEmitter<PaginatorState>();
  @Input() data: Array<Metadata> = [];
  @Input() loading: boolean;
  @Input() total: number;
  public isSorted: boolean = false;
  public initialValue: any[];
  public pageSize: number = 10;
  public pageSizes: Array<Number> = [5,10,20];

  ngOnInit(): void {
    this.initialValue = this.data;
  }

  onPageSelection(event: PaginatorState) {
    this.pageSize = event.rows;
    this.onPageChange.emit(event);
  }  

  onFilterSelection(event: any) {
    const temp = event;
  }

  onFilterData(event: any, field: string, matchMode: string) {
    let value = event.target.value;

    if (value) {
      this.dataGrid.filter(value, field, matchMode);
    } else {
      this.dataGrid.reset();
    }
  }

  customSort(event: SortEvent) {
    if (this.isSorted == null || this.isSorted == undefined) {
      this.isSorted = true;
      this.sortGridData(event);

    } else if (this.isSorted) {
      this.isSorted = false;
      this.sortGridData(event);

    } else if (this.isSorted == false) {
      this.isSorted = null;
      this.data = this.initialValue;
      this.dataGrid.reset();
    }
  }

  sortGridData(event: SortEvent) {
    event.data?.sort((firstItem, secondItem) => {
      let field = event.field ?? "none";
      let order = event.order ?? 1;
      let value1 = firstItem[field];
      let value2 = secondItem[field];
      let result = null;

      if (!value1 && value2) {
        result = -1;
      } else if (value1 && !value2) {
        result = 1;
      } else if (!value1 && !value2) {
        result = 0;
      } else if (typeof value1 == "string" && typeof value2 == "string") {
        result = value1.localeCompare(value2);
      } else {
        result = value1 < value2 ? -1 : value1 > value2 ? 1 : 0;
      }

      return order * result;
    });
  }
}
