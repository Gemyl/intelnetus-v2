from models import Publication_Db_Model, Author_Db_Model, Organization_Db_Model, Publication_Author_Db_Model, Publication_Organization_Db_Model, Author_Organization_Db_Model
from lib.helpers import get_scopus_fields, get_affiliations_ids, build_keywords_query
from pybliometrics.scopus import AbstractRetrieval, AuthorRetrieval, AffiliationRetrieval
from builders import PublicationBuilder, AuthorBuilder, OrganizationBuilder
from db.requests import expand_column_size
from lib.constants import BLUE, RESET
from requests import get
from tqdm import tqdm
import json
import requests as re

def extract_metadata(keywords, year_published, fields, booleans, api_key, db, is_production_env):

    scopus_fields = get_scopus_fields(fields)
    dois = get_dois(keywords, year_published, scopus_fields, booleans, api_key)

    for doi in tqdm(dois):
        try:
            publication_metadata = AbstractRetrieval(doi, view="FULL")
            publication_record = PublicationBuilder(publication_metadata, year_published, doi)
            publication = Publication_Db_Model(
                id = publication_record.id, 
                doi = publication_record.doi,
                year = publication_record.year,
                title = publication_record.title,
                journal = publication_record.journal,
                abstract = publication_record.abstract,
                keywords = publication_record.keywords,
                fields = publication_record.fields,
                fields_abbreviations = publication_record.fields_abbreviations[:10],
                citations_count = publication_record.citations_count,
                authors_number = publication_record.authors_number,
                organizations_number = publication_record.affiliations_number
            )

            while True:
                try:
                    db.session.add(publication)
                    db.session.commit()

                    currrent_publication_id = publication_record.id
                    publication_error_code = 0
                    break

                except Exception as publication_inserting_error:
                    db.session.rollback()

                    publication_error_code = 1
                    publication_error_message = publication_inserting_error.args[0]

                    if "Duplicate entry" not in str(publication_error_message):

                        if "Data too long" in str(publication_error_message):
                            pattern = r'\'+(.*?)\''
                            column_name = re.search(pattern, str(publication_error_message), re.IGNORECASE).group(1)

                            publication_attributes_sizes = {
                                "doi": len(publication_record.doi),
                                "title": len(publication_record.title),
                                "abstract": len(publication_record.abstract),
                                "keywords": len(publication_record.keywords),
                                "journal": len(publication_record.journal),
                                "fields": len(publication_record.fields),
                                "fields_abbreviations": len(publication_record.fields_abbreviations)
                            }

                            expand_column_size(publication_attributes_sizes[column_name], 'publications', column_name, is_production_env)
                    
                        else:
                            publication_error_code = 2
                            print(f"{BLUE}Publication Metadatata Inserting Error Info:{RESET}\n"
                                f"DOI: {doi}\n"
                                f"Error: {str(publication_error_message)}")
                            break
                    else:
                        break

            if (publication_error_code == 0):                
                try:
                    authors = AbstractRetrieval(doi).authors

                    for author in authors:
                        author_metadata = AuthorRetrieval(author[0])
                        author_record = AuthorBuilder(author_metadata)
                        author = Author_Db_Model(
                            id = author_record.id,
                            scopus_id = author_record.scopus_id,
                            orcid_id = author_record.orcid_id,
                            first_name = author_record.first_name,
                            last_name = author_record.last_name,
                            study_fields = author_record.fields_of_study,
                            affiliations = author_record.affiliations,
                            h_index = author_record.h_index,
                            citations_count = author_record.citations_count
                        )

                        while True:
                            try:
                                db.session.add(author)
                                db.session.commit()

                                current_author_id = author_record.id
                                author_error_code = 0
                                break

                            except Exception as author_inserting_error:   
                                db.session.rollback()       

                                author_error_code = 1
                                author_error_message = author_inserting_error.args[0]

                                if "Duplicate entry" not in author_error_message:
                                    if "Data too long" in author_error_message:
                                        pattern = r'\'+(.*?)\''
                                        column_name = re.search(pattern, author_error_message, re.IGNORECASE).group(1)  

                                        author_attributes_sizes = {
                                            "first_name": len(author_record.first_name),
                                            "last_name": len(author_record.last_name),
                                            "study_fields": len(author_record.fields_of_study),
                                            "affiliations": len(author_record.affiliations)
                                        }     

                                        expand_column_size(author_attributes_sizes[column_name], 'authors', column_name, is_production_env)

                                    else:
                                        author_error_code = 2
                                        print(f"{BLUE}Author Inserting Error Info:{RESET}\n"
                                            f"DOI: {doi}\n"
                                            f"Error: {author_error_message}")
                                        break

                                else:
                                    author_result = Author_Db_Model.query.filter_by(scopus_id = author_record.scopus_id).first()
                                    current_author_id = author_result.id
                                    break

                        if (author_error_code in [0, 1]):
                            publication_author = Publication_Author_Db_Model(
                                publication_id = currrent_publication_id,
                                author_id = current_author_id
                            )

                            db.session.add(publication_author)
                            db.session.commit()

                            try:
                                authors = AbstractRetrieval(doi).authors

                                for author in authors:
                                    author_id = str(AuthorRetrieval(author[0]).identifier)
                                    affiliations = get_affiliations_ids(author[4])

                                    if ((affiliations != "-") & (author_id == author_record.scopus_id)):
                                        for affil in affiliations:
                                            organization_metadata = AffiliationRetrieval(int(affil), view="STANDARD")
                                            organization_record = OrganizationBuilder(organization_metadata)
                                            organization = Organization_Db_Model(
                                                id = organization_record.id,
                                                scopus_id = organization_record.scopus_id,
                                                name = organization_record.name,
                                                primary_type = organization_record.type_1,
                                                secondary_type = organization_record.type_2,
                                                address = organization_record.address,
                                                city = organization_record.city,
                                                country = organization_record.country
                                            )

                                            while True:
                                                try:
                                                    db.session.add(organization)
                                                    db.session.commit()

                                                    current_organization_id = organization_record.id
                                                    affliliation_error_code = 0
                                                    break

                                                except Exception as organization_inserting_error:
                                                    db.session.rollback()

                                                    affliliation_error_code = 1
                                                    organization_error_message = organization_inserting_error.args[0];

                                                    if "Duplicate entry" not in organization_error_message:
                                                        if "Data too long" in organization_error_message:
                                                            pattern = r'\'+(.*?)\''
                                                            column_name = re.search(pattern, organization_error_message, re.IGNORECASE).group(1)
                                                            
                                                            affiliation_attributes_sizes = {
                                                                "name": len(organization_record.name),
                                                                "address": len(organization_record.address),
                                                                "city": len(organization_record.city),
                                                                "country": len(organization_record.country)
                                                            }

                                                            expand_column_size(affiliation_attributes_sizes[column_name], "organizations", column_name, is_production_env)

                                                        else:
                                                            affliliation_error_code = 2
                                                            print(f"{BLUE}Organization Inserting Error Info:{RESET}\n"
                                                                f"DOI: {doi}\n"
                                                                f"Organization Scopus ID {organization_record.scopus_id}\n"
                                                                f"Error: {organization_error_message}")
                                                            break

                                                    else:
                                                        organization_result = Organization_Db_Model.query.filter_by(scopus_id = organization_record.scopus_id).first()
                                                        current_organization_id = organization_result.id
                                                        break

                                            if (affliliation_error_code in [0, 1]):
                                                try:
                                                    publication_organization = Publication_Organization_Db_Model(
                                                        publication_id = currrent_publication_id,
                                                        organization_id = current_organization_id
                                                    )

                                                    db.session.add(publication_organization)
                                                    db.session.commit()

                                                except Exception as publication_affiliation_inserting_error:
                                                    db.session.rollback()

                                                    if "Duplicate entry" not in publication_affiliation_inserting_error.args[0]:
                                                        print(f"{BLUE}Publications - Organizations Inserting Error Info:{RESET}\n"
                                                            f"DOI: {doi}\n"
                                                            f"Organization Scopus ID {organization_record.scopus_id}\n"
                                                            f"Error: {publication_affiliation_inserting_error.args[0]}")

                                                try:
                                                    author_organization = Author_Organization_Db_Model(
                                                        author_id = current_author_id,
                                                        organization_id = current_organization_id,
                                                        year = year_published
                                                    )

                                                    db.session.add(author_organization)
                                                    db.session.commit()

                                                except Exception as author_affiliation_inserting_error:
                                                    db.session.rollback()

                                                    if "Duplicate entry" not in author_affiliation_inserting_error.args[0]:
                                                        print(f"{BLUE}Authors - Organizations Inserting Error Info:{RESET}\n"
                                                            f"DOI: {doi}\n"
                                                            f"Organization Scopus ID {organization_record.scopus_id}\n"
                                                            f"Error: {author_affiliation_inserting_error.args[0]}")

                            except Exception as affiliation_ogranization_error:
                                print(f"{BLUE}Organization Retrieving Error Info:{RESET}\n"
                                    f"DOI: {doi}\n"
                                    f"Organization Scopus ID {organization_record.scopus_id}\n"
                                    f"Error: {str(affiliation_ogranization_error)}")
                                pass

                except Exception as author_retrieving_error:
                    print(f"{BLUE}Author Retrieving Error Info:{RESET}\n"
                        f"DOI: {doi}\n"
                        f"Error: {str(author_retrieving_error)}")
                    pass

        except Exception as publication_retrieving_error:
            print(f"{BLUE}Publication Retrieving Error Info:{RESET}\n"
                f"DOI: {doi}\n"
                f"Error: {str(publication_retrieving_error)}")
            pass


def get_dois(keywords, yearPublished, fields, booleans, apiKey):

    # DOIs list
    dois = []

    # query parameters
    count = '&count=25'
    terms = f'( {build_keywords_query(keywords, booleans)} )'
    scope = 'TITLE-ABS-KEY'
    view = '&view=standard'
    sort = '&sort=citedby_count'
    date = '&date=' + str(yearPublished)
    scopusAPIKey = f'&apiKey={apiKey}'
    scopusBaseUrl = 'http://api.elsevier.com/content/search/scopus?'

    # retrieving publications DOIs
    print(f"Retrieving DOIs for year {yearPublished}.")
    for field in tqdm(fields):
        
        errorCounter = 0
        startIndex = 0
        while True:
            start = f"&start={startIndex}"
            currentField = f"&subj={field}"
            
            # building GET query
            query = 'query=' + scope + terms + date + start + \
                count + sort + currentField + scopusAPIKey + view
            url = scopusBaseUrl + query

            req = get(url)
            # if request is successful, get DOIs
            if req.status_code == 200:
                content = json.loads(req.content)['search-results']
                totalResults = int(content['opensearch:totalResults'])
                startIndex = int(content['opensearch:startIndex'])
                entries = content['entry']
            # else print the error cause
            else:
                Error = json.loads(req.content)['service-error']['status']
                print(req.status_code, Error['statusText'])
                errorCounter += 1

            for entry in entries:
                try:
                    TempDOI = entry['prism:doi']
                    dois.append(str(TempDOI))
                except:
                    pass

            remainingData = totalResults - startIndex - len(entries)

            # if there are any records remained, update startIndex and start the next loop
            if ((remainingData > 0) & (errorCounter < 10)):
                startIndex += 25
                print(f"Field: {field}, Total Results: {totalResults}, Fetched Results: {startIndex}, Remaining Results: {remainingData}")
            
            # else exit the loop and continue with the next subject
            else:
                break

    return dois            