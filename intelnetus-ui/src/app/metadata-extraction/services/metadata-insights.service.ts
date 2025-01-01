import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { 
  GetMetadataInsightsRequest,
  GetMetadataInsightsResponse
} from '../models/metadata-insights.model';

@Injectable({
  providedIn: 'root'
})
export class MetadataInsightsService {

  constructor(
    private _http: HttpClient
  ) { }

  getPublicationsPerCountry(request: GetMetadataInsightsRequest): Observable<GetMetadataInsightsResponse> {
    const url = `${environment.MetadataApi}/get-insights`;
    const params = new HttpParams()
      .set("keywords", request.keywords)
      .set("operators", request.operators)
      .set("startYear", request.startYear)
      .set("endYear", request.endYear)
      .set("fields", request.fields)

    return this._http.get<GetMetadataInsightsResponse>(url, {params: params});
  }
}
