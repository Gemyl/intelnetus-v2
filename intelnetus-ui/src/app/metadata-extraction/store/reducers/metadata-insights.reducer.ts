import { createReducer, on } from "@ngrx/store";
import { MetadataInsightsState } from "../../models/metadata-insights.model";
import { GetMetadataInsightsSuccessAction } from "../actions/metadata-insights.actions";

const initialState: MetadataInsightsState = {
    publicationsNumberPerCountry: {},
    publicationsCitationsNumberPerField: {},
    fieldsCitationsPerYear: {}
}

export const metadataInsightsReducer = createReducer(
    initialState,
    on(GetMetadataInsightsSuccessAction, (state, { 
        publicationsNumberPerCountry, 
        publicationsCitationsNumberPerField, 
        fieldsCitationsPerYear
    }) => { 
        return { 
            ...state,
            publicationsNumberPerCountry,
            publicationsCitationsNumberPerField,
            fieldsCitationsPerYear  
        } 
    })
)