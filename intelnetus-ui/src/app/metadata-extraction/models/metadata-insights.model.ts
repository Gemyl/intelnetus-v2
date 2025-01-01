export class GetMetadataInsightsRequest {
    public keywords: string;
    public operators: string;
    public startYear: string;
    public endYear: string;
    public fields: string;

    constructor(
        keywords: string = "",
        operators: string = "",
        startYear: string = "",
        endYear: string = "",
        fields: string = ""
    ) {
        this.keywords = keywords;
        this.operators = operators;
        this.startYear = startYear;
        this.endYear = endYear;
        this.fields = fields;
    }
}

export interface GetMetadataInsightsResponse {
    successful: boolean,
    hasResult: boolean,
    errorMessage?: string,
    data: MetadataInsightsState
}

export interface MetadataInsightsState {
    publicationsNumberPerCountry: Record<string, number>,
    publicationsCitationsNumberPerField: Record<string, number>,
    fieldsCitationsPerYear: Record<string, Record<string, number>> 
}