import { createReducer, on } from "@ngrx/store";
import { MetadataState } from "../../models/metadata-extraction.model";
import {
    LoadMetadataSuccess
} from "../actions/metadata-extraction.action";

export const initialState: MetadataState = {
    data: [],
    variants: {
        publicationsVariants: {
            originals: [],
            duplicates: [],
        },
        authorsVariants: {
            originals: [],
            duplicates: []
        },
        organizationsVariants: {
            originals: [],
            duplicates: []
        }
    },
    total: 0
}

export const metadataExtractionReducer = createReducer(
    initialState,
    on(LoadMetadataSuccess, (state, { data, variants, total }) => { return { ...state, data, variants, total }})
);