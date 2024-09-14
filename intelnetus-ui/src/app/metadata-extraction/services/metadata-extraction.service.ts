import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { HttpClient, HttpParams } from '@angular/common/http';
import { GetMetadataRequest } from '../models/metadata-extraction.model';

@Injectable({
  providedIn: 'root'
})
export class MetadataExtractionService {

  constructor(
    private http: HttpClient
  ) { }

  loadMetadata(data: GetMetadataRequest): Observable<any> {
    const url = `${environment.MetadataApi}/get-metadata`;
    const params = new HttpParams()
    .set('keywords', data.keywords)
    .set('operators', data.operators)
    .set('startYear', data.startYear)
    .set('endYear', data.endYear)
    .set('fields', data.fields)
    .set('pageSize', data.pageSize)
    .set('offset', data.offset)

    return this.http.get(url, {params: params});
  }
}
