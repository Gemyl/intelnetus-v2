import { Component, ViewChild, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { SortEvent } from 'primeng/api';
import { Table } from 'primeng/table';
import { GridFilter, Metadata } from '../../models/metadata-extraction.model';
import { PaginatorState } from 'primeng/paginator';
import { Entity } from '../../models/metadata-extraction.model';

@Component({
  selector: 'app-metadata-table',
  templateUrl: './metadata-table.component.html',
  styleUrls: []
})
export class MetadataTableComponent implements OnInit {
  @ViewChild("dt") dataGrid: Table;
  @Output() onPageChange: EventEmitter<PaginatorState> = new EventEmitter<PaginatorState>();
  @Output() onFiltersChange: EventEmitter<string> = new EventEmitter<string>();
  @Input() data: Array<Metadata> = [];
  @Input() loading: boolean;
  @Input() total: number;
  public isSorted: boolean = false;
  public initialValue: any[];
  public pageSize: number = 10;
  public pageSizes: Array<Number> = [5,10,20];
  public entity = Entity;
  public filters: Array<GridFilter> = [];

  ngOnInit(): void {
    this.initialValue = this.data;
  }

  onPageSelection(event: PaginatorState) {
    this.pageSize = event.rows;
    this.onPageChange.emit(event);
  }  

  onFilterData(event: any, field: string, entity: string, matchMode: string) {
    let value = event.target.value;
    const filters = this.dataGrid.filters as any;

    let filterValues = Object.keys(filters)
    .map((key => {
      return {
        field: key,
        value: field == key ? value : filters[key].value,
        entity: entity
      }
    }));

    const filter = this.filters.find(f => f.field == field);
    if(!filter) {
      this.filters.push(filterValues.find(f => f.field == field));
    } else if(value) {
      filter.value = value;
    } else {
      this.filters = this.filters.filter(f => f.field != field);
    }

    this.onFiltersChange.emit(JSON.stringify(this.filters));

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
