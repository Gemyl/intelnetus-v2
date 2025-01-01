import { MetadataState } from "./metadata-extraction/models/metadata-extraction.model"
import { MetadataInsightsState } from "./metadata-extraction/models/metadata-insights.model"

export class AppState {
    metadataState: MetadataState
    metadataInsightsState: MetadataInsightsState
}
