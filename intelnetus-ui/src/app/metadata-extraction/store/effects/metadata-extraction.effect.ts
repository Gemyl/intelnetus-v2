import { Injectable } from "@angular/core";
import { Actions, createEffect, ofType } from "@ngrx/effects";
import { map, switchMap } from "rxjs";
import { MetadataExtractionService } from "../../services/metadata-extraction.service";
import { 
    LoadMetadata,
    LoadMetadataSuccess
} from "../actions/metadata-extraction.action";

@Injectable()
export class MetadataExtractionEffects {
    constructor(
        private actions$: Actions,
        private _metadataExtractionService: MetadataExtractionService
    ) {}

    loadMetadata$ = createEffect(() => (
        this.actions$.pipe(
            ofType(LoadMetadata),
            switchMap((action) => 
                this._metadataExtractionService.loadMetadata(action).pipe(
                    map((response) => {
                        return LoadMetadataSuccess({data: response.data, variants: response.variants, total: response.total});
                    })
                )
            )
        )
    ));
}