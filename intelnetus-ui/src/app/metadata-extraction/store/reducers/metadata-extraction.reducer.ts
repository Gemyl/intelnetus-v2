import { createReducer, on } from "@ngrx/store";
import { MetadataState } from "../../models/metadata-extraction.model";
import { 
    LoadMetadata, 
    LoadMetadataSuccess
} from "../actions/metadata-extraction.action";

export const initialState: MetadataState = {
    data: [],
    total: 0
}

export const metadataExtractionReducer = createReducer(
    initialState,
    on(LoadMetadata, (state) => {return state}),
    on(LoadMetadataSuccess, (state, { data, total }) => { return { ...state, data, total }})
);