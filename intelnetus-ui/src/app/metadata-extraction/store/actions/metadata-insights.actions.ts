import { createAction, props } from "@ngrx/store";
import { GetMetadataInsightsRequest, MetadataInsightsState } from "../../models/metadata-insights.model";

export const GetMetadataInsightsAction = createAction('[Metadata Insights] Get publications number per country', props<GetMetadataInsightsRequest>());
export const GetMetadataInsightsSuccessAction = createAction('[Metadata Insights] Get publications number per country success', props<MetadataInsightsState>())