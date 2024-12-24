from models import Publication_Db_Model, Author_Db_Model, Organization_Db_Model, Publication_Variant_Db_Model, Author_Variant_Db_Model, Organization_Variant_Db_Model
from fuzzywuzzy.fuzz import ratio
from pybliometrics.scopus import AffiliationRetrieval
from lib.helpers import get_most_recent_profile

def get_publications_duplicates(db):

    ids = []
    dois = []
    titles = []
    abstracts = []
    keywords = []
    fields = []
    citations_counts = []
    primary_variants = []
    secondary_variants = []

    publications = Publication_Db_Model.query.order_by(Publication_Db_Model.title).all()
    for publication in publications:
        ids.append(publication.id)
        dois.append(publication.doi)
        titles.append(publication.title)
        abstracts.append(publication.abstract)
        keywords.append(publication.keywords)
        fields.append(publication.fields)
        citations_counts.append(publication.citations_count)

    for i in range(len(ids)-1):
        for j in range(i+1, len(ids)):

            if((ratio(titles[i], titles[j]) > 85) & (ratio(abstracts[i], abstracts[j]) > 85) 
            & (ratio(keywords[i], keywords[j]) > 85) & (ratio(fields[i], fields[j]) > 85)):

                if (citations_counts[i] > citations_counts[j]):
                    if((ids[i] in secondary_variants) & (ids[j] not in secondary_variants)):
                        index = secondary_variants.index(ids[i])
                        primary_variants.append(primary_variants[index])
                        secondary_variants.append(ids[j])

                    elif(ids[j] not in secondary_variants):
                        primary_variants.append(ids[i])
                        secondary_variants.append(ids[j])

                else:
                    if((ids[j] in secondary_variants) & (ids[i] not in secondary_variants)):
                        index = secondary_variants.index(ids[j])
                        primary_variants.append(primary_variants[index])
                        secondary_variants.append(ids[i])
                    
                    elif(ids[i] not in secondary_variants):
                        primary_variants.append(ids[j])
                        secondary_variants.append(ids[i])

            else:
                break

    for i in range(len(primary_variants)):
        try:
            publication_variant = Publication_Variant_Db_Model(
                first_variant_id = primary_variants[i],
                second_variant_id = secondary_variants[i]
            )

            db.session.add(publication_variant)
            db.session.commit()

        except:
            db.session.rollback()
            pass


def get_authors_duplicates(db):

    ids = []
    orcid_ids = []
    last_names = []
    first_names = []
    subjected_areas = []
    affiliation_history = []
    citations_counts = []
    primary_variants = []
    secondary_variants = []

    authors = Author_Db_Model.query.order_by(Author_Db_Model.last_name).all()
    for author in authors:
        ids.append(author.id)
        orcid_ids.append(author.orcid_id)
        first_names.append(author.first_name)
        last_names.append(author.last_name)
        subjected_areas.append(author.study_fields)
        affiliation_history.append(author.affiliations)
        citations_counts.append(author.citations_count)

    for i in range(len(ids) - 1):
        for j in range(i + 1, len(ids)):

            if (((ratio(last_names[i], last_names[j]) > 90) & (ratio(first_names[i], first_names[j]) > 90)) 
                & (((orcid_ids[i] is not None) & (orcid_ids[j] is not None) & (orcid_ids[i] == orcid_ids[j])) 
                | (ratio(subjected_areas[i], subjected_areas[j]) > 90) & (ratio(affiliation_history[i], affiliation_history[j]) > 90))):

                if ((citations_counts[i] > citations_counts[j]) ):
                    if((ids[i] in secondary_variants) & (ids[j] not in secondary_variants)):
                        index = secondary_variants.index(ids[i])
                        primary_variants.append(primary_variants[index])
                        secondary_variants.append(ids[j])

                    elif(ids[j] not in secondary_variants):
                        primary_variants.append(ids[i])
                        secondary_variants.append(ids[j])

                else:
                    if((ids[j] in secondary_variants) & (ids[i] not in secondary_variants)):
                        index = secondary_variants.index(ids[j])
                        primary_variants.append(primary_variants[index])
                        secondary_variants.append(ids[i])

                    elif(ids[i] not in secondary_variants):
                        primary_variants.append(ids[j])
                        secondary_variants.append(ids[i])
                      
            else:
                break

    for i in range(len(primary_variants)):
        try:
            author_variant = Author_Variant_Db_Model(
                first_variant_id = primary_variants[i],
                second_variant_id = secondary_variants[i]
            )

            db.session.add(author_variant)
            db.session.commit()

        except:
            db.session.rollback()
            pass


def get_organizations_duplicates(db):

    ids = []
    names = []
    scopus_ids = []
    addresses = []
    primary_variants = []
    secondary_variants = []

    organizations = Organization_Db_Model.query.order_by(Organization_Db_Model.name).all()
    for organization in organizations:
        ids.append(organization.id)
        names.append(organization.name)
        scopus_ids.append(organization.scopus_id)
        addresses.append(organization.address)

    for i in range(len(names)-1):
        for j in range(i+1, len(names)):
            
            if (((ratio(names[i], names[j]) > 85) | (names[i] in names[j]) | (names[j] in names[i])) 
                & (addresses[i] == addresses[j])):
                
                first_date = AffiliationRetrieval(int(scopus_ids[i])).date_created
                second_date = AffiliationRetrieval(int(scopus_ids[j])).date_created

                if (get_most_recent_profile(first_date, second_date) == first_date):
                    if((ids[i] in secondary_variants) & (ids[j] not in secondary_variants)):
                        index = secondary_variants.index(ids[i])
                        primary_variants.append(primary_variants[index])
                        secondary_variants.append(ids[j])
                    
                    elif(ids[j] not in secondary_variants):
                        primary_variants.append(ids[i])
                        secondary_variants.append(ids[j])
                
                else:
                    if((ids[j] in secondary_variants) & (ids[i] not in secondary_variants)):
                        index = secondary_variants.index(ids[j])
                        primary_variants.append(primary_variants[index])
                        secondary_variants.append(ids[i])
                    
                    elif(ids[i] not in secondary_variants):
                        primary_variants.append(ids[j])
                        secondary_variants.append(ids[i])
                    
            else:
                break

    for i in range(len(primary_variants)):
        try:
            organization_variant = Organization_Variant_Db_Model(
                first_variant_id = primary_variants[i],
                second_variant_id = secondary_variants[i]
            )

            db.session.add(organization_variant)
            db.session.commit()

        except:
            db.session.rollback()
            pass