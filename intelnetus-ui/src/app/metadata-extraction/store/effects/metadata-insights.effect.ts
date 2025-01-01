import { Injectable } from "@angular/core";
import { Actions, createEffect, ofType } from "@ngrx/effects";
import { map, switchMap } from "rxjs";
import { MetadataInsightsService } from "../../services/metadata-insights.service";
import { GetMetadataInsightsAction, GetMetadataInsightsSuccessAction } from "../actions/metadata-insights.actions";

@Injectable()
export class MetadataInsightsEffects {

    constructor(
        private actions$: Actions,
        private _metadataInsightsService: MetadataInsightsService
    ) {}

    getPublicationsNumberPerCountry$ = createEffect(() => (
        this.actions$.pipe(
            ofType(GetMetadataInsightsAction),
            switchMap((action) => (
                this._metadataInsightsService.getPublicationsPerCountry(action).pipe(
                    map((response) => {
                        return GetMetadataInsightsSuccessAction({
                            publicationsNumberPerCountry: response.data.publicationsNumberPerCountry,
                            publicationsCitationsNumberPerField: response.data.publicationsCitationsNumberPerField,
                            fieldsCitationsPerYear: response.data.fieldsCitationsPerYear
                        })
                    })
                )
            ))
        )
    ));
}