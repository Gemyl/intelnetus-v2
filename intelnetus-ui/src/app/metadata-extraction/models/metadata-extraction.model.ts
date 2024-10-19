export enum Entity {
    PUBLICATION = "publications",
    AUTHOR = "authors",
    ORGANIZATION = "organizations"
}

export interface GridFilter {
    field: string,
    value: string | number,
    entity: string
}

export interface Field {
    id: string,
    name: string,
    selected: boolean
}

export interface MetadataState {
    data: Metadata[];
    variants: Variants;
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

export interface PublicationVariants {
    id: string;
    type: number;
    title: string;
    citationsCount: number;
}

export interface AuthorVariants {
    id: string;
    type: number;
    firstName: string;
    lastName: string;
    hIndex: string;
    citationsCount: number;
}

export interface OrganizationVariants {
    id: string;
    type: number;
    name: string;   
}

export interface Variant {
    originals: Array<PublicationVariants | AuthorVariants | OrganizationVariants>;
    duplicates: Array<PublicationVariants | AuthorVariants | OrganizationVariants>
}

export interface Variants {
    publicationsVariants: Variant;
    authorsVariants: Variant;
    organizationsVariants: Variant;
}

export interface GetMetadataResponse {
    successful: boolean;
    hasResult: boolean;
    data: Array<Metadata>;
    variants: Variants;
    total: number;
}

export class GetMetadataRequest {
    public keywords: string;
    public operators: string;
    public startYear: string;
    public endYear: string;
    public fields: string;
    public pageSize: number;
    public offset: number;
    public filterValue: string;
    public exclude: string;

    constructor(
        keywords: string = "",
        operators: string = "",
        startYear: string = "",
        endYear: string = "",
        fields: string = "",
        pageSize: number = 10,
        offset: number = 0,
        filterValue: string = "[]",
        exclude: string = "[]"
    ) {
        this.keywords = keywords;
        this.operators = operators;
        this.startYear = startYear;
        this.endYear = endYear;
        this.fields = fields;
        this.pageSize = pageSize;
        this.offset = offset;
        this.filterValue = filterValue;
        this.exclude = exclude;
    }
}