export interface Field {
    id: string,
    name: string,
    selected: boolean
}

export interface MetadataState {
    data: Metadata[];
    total: number;
}

export interface Metadata {
    publicationId: string;
    publicationDoi: string;
    publicationYear: string;
    publicationTitle: string;
    publicationAbstract: string;
    publicationKeywords: string;
    publicationFields: string;
    publicationJournal: string;
    publicationCitationsCount: string;
    publicationAuthorsNumber: number;
    publicationAffiliationsNumber: string;

    authorId: string;
    authorScopusId: string;
    authorOrcid: string;
    authorFirstName: string;
    authorLastName: string;
    authorFieldsOfStudy: string;
    authorAffiliations: string;
    authorCitationsCount: string;

    organizationId: string;
    organizationScopusId: string;
    organizationName: string;
    organizationPrimaryType: string;
    organizationSecondaryType: string;
    organizationAddress: string;
    organizationCity: string;
    organizationCountry: string;
}

export class GetMetadataRequest {
    public keywords: string;
    public operators: string;
    public startYear: string;
    public endYear: string;
    public fields: string;
    public pageSize: number;
    public offset: number;

    constructor(
        keywords: string,
        operators: string,
        startYear: string,
        endYear: string,
        fields: string,
        pageSize: number,
        offset: number
    ) {
        this.keywords = keywords;
        this.operators = operators;
        this.startYear = startYear;
        this.endYear = endYear;
        this.fields = fields;
        this.pageSize = pageSize;
        this.offset = offset;
    }
}