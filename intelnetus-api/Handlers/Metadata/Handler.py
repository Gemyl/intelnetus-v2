# import os
# os.environ['PYB_CONFIG_FILE'] = "/app/.pybliometrics/config.ini"
from pybliometrics.scopus import AbstractRetrieval, AuthorRetrieval, AffiliationRetrieval, PlumXMetrics
from models import Publication_Db_Model, Author_Db_Model, Organization_Db_Model, Publication_Author_Db_Model, Publication_Organization_Db_Model, Author_Organization_Db_Model, Publication_Variant_Db_Model, Author_Variant_Db_Model, Organization_Variant_Db_Model
from Handlers.GenericData.Handler import get_sql_syntax, remove_common_words, get_safe_attribute, get_affiliations_ids
from Services.Scopus.Service import get_dois
from Services.Database.Service import expand_column_size
from fuzzywuzzy.fuzz import ratio
from tqdm import tqdm
import uuid
import re

BLUE = "\033[1;34m"
RESET = "\033[0m"
MAX_COLUMN_SIZE = 5000
ORGANIZATIONS_TYPES_KEYWORDS = {
    "university": ['university', 'college', 'departement'],
    "academy": ['academy', 'academic', 'academia'],
    "school": ['school', 'faculty'],
    "research": ['research', 'researchers'],
    "business": ['inc', 'ltd', 'corporation'],
    "association": ['association'],
    "non-profit": ['non-profit'],
    "government": ['government', 'gov', 'public', 'state', 'national', 'federal', 'federate', 'confederate', 'royal'],
    "international": ['international']
}
SCOPUS_FIELDS = ['AGRI', 'ARTS', 'BIOC', 'BUSI', 'CENG', 'CHEM', 
    'COMP','DECI', 'DENT', 'EART', 'ECON', 'ENER', 'ENGI', 'ENVI',
    'HEAL', 'IMMU', 'MATE', 'MATH', 'MEDI', 'MULT', 'NEUR', 'NURS', 
    'PHAR', 'PHYS', 'PSYC', 'SOCI', 'VETE']
COMMON_WORDS = ['a', 'an', 'the', 'and', 'or', 'but', 'if', 'of', 'at', 'by', 'for', 'with', 'about',
    'to', 'from', 'in', 'on', 'up', 'out', 'as', 'into', 'through', 'over', 'after', 'under',
    'i', 'you', 'he', 'she', 'it', 'we', 'they', 'is', 'are', 'was', 'were', 'has', 'had',
    'will', 'be', 'not', 'would', 'should', 'before', 'few', 'many', 'much', 'so', 'furthermore'] 

class Publication_Metadata_Handler:
    def __init__(self, publication_data, year, doi):
        self.id = str(uuid.uuid4())
        self.doi = doi
        self.year = year
        self.title = get_sql_syntax(
            get_safe_attribute(publication_data, 'title', 'string')
        )
        
        self.journal = get_sql_syntax(
            get_safe_attribute(publication_data, 'publicationName', 'string')
        )
        
        self.abstract = get_sql_syntax(
            remove_common_words(
                Publication_Metadata_Handler.get_abstract(
                    get_safe_attribute(publication_data, 'abstract', 'string'),
                    get_safe_attribute(publication_data, 'description', 'string')
                ),
                COMMON_WORDS
            )
        )
        
        self.keywords = get_sql_syntax(
            Publication_Metadata_Handler.get_keywords(
                get_safe_attribute(publication_data, 'authkeywords', 'string')
            )
        )
        
        self.fields = get_sql_syntax(
            Publication_Metadata_Handler.get_fields(
                get_safe_attribute(publication_data, 'subject_areas', 'string')
            )
        )
        
        self.fields_abbreviations = get_sql_syntax(
            Publication_Metadata_Handler.get_fields_abbreviations(
                get_safe_attribute(publication_data, 'subject_areas', 'string')
            )
        )
        
        self.citations_count = Publication_Metadata_Handler.get_maximum_citations_count(
            get_safe_attribute(publication_data, 'citedby_count', 'number'),
            doi
        )
        
        self.authors_number = Publication_Metadata_Handler.get_authors_number(
            get_safe_attribute(publication_data, 'authors', 'list')
        )
        
        self.affiliations_number = Publication_Metadata_Handler.get_affiliations_number(
            get_safe_attribute(publication_data, 'affiliation', 'list')
        )

    def get_abstract(abstract, description):
        if abstract != None:
            item = get_sql_syntax(abstract)
        
        elif description != None:
            item = get_sql_syntax(description)
        
        else:
            item = "-"

        if (len(item) > MAX_COLUMN_SIZE):
            item = item[:MAX_COLUMN_SIZE]

        return item
        
    def get_keywords(keywords):
        if keywords != None:
            item = get_sql_syntax(", ".join([keyword for keyword in keywords]))
        else:
            item = "-"

        if (len(item) > MAX_COLUMN_SIZE):
            item = item[:MAX_COLUMN_SIZE]

        return item
    
    def get_fields(fields):
        if fields != None:
            item = get_sql_syntax(", ".join([field[0].lower() for field in fields]))
        else:
            item = "-"

        if (len(item) > MAX_COLUMN_SIZE):
            item = item[:MAX_COLUMN_SIZE]

        return item
        
    def get_fields_abbreviations(fields):
        if fields != None:
            return get_sql_syntax(", ".join([field[1].lower() for field in fields]))
        else:
            return "-"
    
    def get_maximum_citations_count(citations_count, doi):
        max_citations = citations_count
        plumx_citations = PlumXMetrics(doi, id_type='doi').citation

        if plumx_citations != None:
            if max_citations != 999999:
                plumx_citations = max([citation[1] for citation in plumx_citations])
                max_citations = max(max_citations, plumx_citations)
            else:
                max_citations = max([citation[1] for citation in plumx_citations])

        return max_citations
    
    def get_authors_number(authors):
        if ((authors == "-") | (authors == None)):
            return 0
        
        return len(authors)
    
    def get_affiliations_number(affiliations):
        if ((affiliations == "-") | (affiliations == None)):
            return 0

        return len(affiliations)
    

class Author_Metadata_Handler:
    def __init__(self,author_data):
        self.id = str(uuid.uuid4())
        self.scopus_id = str(get_safe_attribute(author_data, 'identifier', 'string'))
        self.orcid_id = get_safe_attribute(author_data, 'orcid', 'string')
        self.first_name = get_sql_syntax(
            get_safe_attribute(author_data, 'given_name', 'string')
        )
        
        self.last_name = get_sql_syntax(
            get_safe_attribute(author_data, 'surname', 'string')
        )
        
        self.h_index = get_safe_attribute(author_data, 'h_index', 'number')
        self.fields_of_study = get_sql_syntax(
            Author_Metadata_Handler.get_fields(get_safe_attribute(author_data, 'subject_areas', 'string'))
        )
        
        self.citations_count = get_safe_attribute(author_data, 'cited_by_count', 'number')
        self.affiliations = get_sql_syntax(
            Author_Metadata_Handler.get_affiliations(get_safe_attribute(author_data, 'affiliation_history', 'string'))
        )

    def get_affiliations(affiliations):
        if ((affiliations == "-") | (affiliations == None)):
            return "-"

        affiliations_history = []
        for affiliation in affiliations:
            if ((affiliation.preferred_name not in affiliations_history) & (affiliation.preferred_name != None)):
                if (affiliation.parent == None):
                    affiliations_history.append(affiliation.preferred_name)
                else:
                    affiliations_history.append(affiliation.preferred_name + ' - ' + affiliation.parent_preferred_name)
                    affiliations_history.append(affiliation.parent_preferred_name)

        affiliations_history_str = ', '.join(affiliations_history).replace("\'", " ")
        if (len(affiliations_history_str) > MAX_COLUMN_SIZE):
            affiliations_history_str = affiliations_history_str[:MAX_COLUMN_SIZE]
        
        affiliations_history_str = get_sql_syntax(affiliations_history_str)

        return affiliations_history_str
    
    def get_fields(fields):
        if (fields == "-") | (fields == None):
            return "-"
        
        fields_str = ", ".join([field[0].lower() for field in fields])
        if (len(fields_str) > MAX_COLUMN_SIZE):
            fields_str = fields_str[:MAX_COLUMN_SIZE]

        fields_str = get_sql_syntax(fields_str)
        
        return fields_str
        

class Organization_Metadata_Handler:
    def __init__(self, organization_data):
        self.id = str(uuid.uuid4())
        self.scopus_id = str(get_safe_attribute(organization_data, 'identifier', 'string'))
        self.name = get_sql_syntax(
            get_safe_attribute(organization_data, 'affiliation_name', 'string')
        )
        
        self.type_1, self.type_2 = Organization_Metadata_Handler.get_affiliation_types(organization_data)
        self.address = get_sql_syntax(
            get_safe_attribute(organization_data, 'address', 'string')
        )
        
        self.city = get_sql_syntax(
            get_safe_attribute(organization_data, 'city', 'string')
        )
        
        self.country = get_sql_syntax(
            get_safe_attribute(organization_data, 'country', 'string')
        )

    def get_affiliation_types(affiliation_record):
        type = get_safe_attribute(affiliation_record, 'org_type', 'string')
        name = get_safe_attribute(affiliation_record, 'affiliation_name', 'string')

        if (type == 'univ') | (type == 'coll') | \
                (len([univ for univ in ORGANIZATIONS_TYPES_KEYWORDS['university'] if univ in name.lower()]) > 0):
            type1 = 'Academic'
            type2 = 'University - College'

        elif (type == 'sch') | \
                (len([sch for sch in ORGANIZATIONS_TYPES_KEYWORDS['school'] if sch in name.lower()]) > 0):
            type1 = 'Academic'
            type2 = 'School'

        elif (type == 'res') | \
                (len([acad for acad in ORGANIZATIONS_TYPES_KEYWORDS['academy'] if acad in name.lower()]) > 0):
            type1 = 'Academic'
            type2 = 'Research Institute'

        elif (type == 'gov') | \
                (len([gov for gov in ORGANIZATIONS_TYPES_KEYWORDS['government'] if gov in name.lower()]) > 0):
            type1 = 'Government'
            type2 = ' '

        elif (type == 'assn') | \
                (len([assn for assn in ORGANIZATIONS_TYPES_KEYWORDS['association'] if assn in name.lower()]) > 0):
            type1 = 'Association'
            type2 = ' '

        elif (type == 'corp') | \
                (len([bus for bus in ORGANIZATIONS_TYPES_KEYWORDS['business'] if bus in name.lower()]) > 0):
            type1 = 'Business'
            type2 = ' '

        elif (type == 'non') | \
                (len([np for np in ORGANIZATIONS_TYPES_KEYWORDS['non-profit'] if np in name.lower()]) > 0):
            type1 = 'non-profit'
            type2 = ' '

        else:
            type1 = "Other"
            type2 = "Other"

        return type1, type2
    

def get_scopus_fields(fields_ids):
    returned_fields = []
    for id in fields_ids:
        returned_fields.append(SCOPUS_FIELDS[int(id)])

    return returned_fields

def process_metadata(keywords, year1, year2, fields, booleans, scopus_api_key, db, is_production_env):

    for year in range(int(year1), int(year2)+1):
        extract_metadata(keywords, year, fields, booleans, scopus_api_key, db, is_production_env)

    get_publications_duplicates(db)
    get_authors_duplicates(db)
    get_organizations_duplicates(db)


def extract_metadata(keywords, year_published, fields, booleans, api_key, db, is_production_env):

    scopus_fields = get_scopus_fields(fields)
    dois = get_dois(keywords, year_published, scopus_fields, booleans, api_key)

    for doi in tqdm(dois):
        try:
            publication_metadata = AbstractRetrieval(doi, view="FULL")
            publication_record = Publication_Metadata_Handler(publication_metadata, year_published, doi)
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
                        author_record = Author_Metadata_Handler(author_metadata)
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
                                            organization_record = Organization_Metadata_Handler(organization_metadata)
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

                if (getMostRecentProfile(first_date, second_date) == first_date):
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
            pass


def getMostRecentProfile(first_date, seconnectiond_date):
    """Return the most recent date between two dates."""
    return max(first_date, seconnectiond_date, key=lambda x: x[::-1])