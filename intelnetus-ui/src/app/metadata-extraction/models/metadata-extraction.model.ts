export class MetadataState {
    data: Metadata[];
    total: number;
}

export class PublicationsMetadata {
    public id: string;
    public doi: string;
    public title: string;
    public year: string;
    public keywords: string;
    public fields: string;
    public citationsCount: string;
}

export class AuthorsMetadata {
    public id: string;
    public firstName: string;
    public lastName: string;
    public fieldsOfStudy: string;
    public citationsCount: string;
    public hIndex: number;
}

export class OrganizationsMetadata {
    public id: string;
    public name: string;
    public primaryType: string;
    public secondaryType: string;
    public city: string;
    public country: string;
}

export class Metadata {
    // PublicationsMetadata attributes
    public publicationId: string;
    public publicationDoi: string;
    public publicationYear: string;
    public publicationTitle: string;
    public publicationAbstract: string;
    public publicationKeywords: string;
    public publicationFields: string;
    public publicationJournal: string;
    public publicationCitationsCount: string;
    public publicationAuthorsNumber: number;
    public publicationAffiliationsNumber: string;

    // AuthorsMetadata attributes
    public authorId: string;
    public authorScopusId: string;
    public authorOrcid: string;
    public authorFirstName: string;
    public authorLastName: string;
    public authorFieldsOfStudy: string;
    public authorAffiliations: string;
    public authorCitationsCount: string;

    // OrganizationsMetadata attributes
    public organizationId: string;
    public organizationScopusId: string;
    public organizationName: string;
    public organizationPrimaryType: string;
    public organizationSecondaryType: string;
    public organizationAddress: string;
    public organizationCity: string;
    public organizationCountry: string;

    constructor(
        publicationsMetadata: PublicationsMetadata,
        authorsMetadata: AuthorsMetadata,
        organizationsMetadata: OrganizationsMetadata
    ) {
        // Map PublicationsMetadata attributes
        this.publicationId = publicationsMetadata.id;
        this.publicationDoi = publicationsMetadata.doi;
        this.publicationYear = publicationsMetadata.year;
        this.publicationTitle = publicationsMetadata.title;
        this.publicationKeywords = publicationsMetadata.keywords;
        this.publicationFields = publicationsMetadata.fields;
        this.publicationCitationsCount = publicationsMetadata.citationsCount;

        // Map AuthorsMetadata attributes
        this.authorId = authorsMetadata.id;
        this.authorFirstName = authorsMetadata.firstName;
        this.authorLastName = authorsMetadata.lastName;
        this.authorFieldsOfStudy = authorsMetadata.fieldsOfStudy;
        this.authorCitationsCount = authorsMetadata.citationsCount;

        // Map OrganizationsMetadata attributes
        this.organizationId = organizationsMetadata.id;
        this.organizationName = organizationsMetadata.name;
        this.organizationPrimaryType = organizationsMetadata.primaryType;
        this.organizationSecondaryType = organizationsMetadata.secondaryType;
        this.organizationCity = organizationsMetadata.city;
        this.organizationCountry = organizationsMetadata.country;
    }
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
