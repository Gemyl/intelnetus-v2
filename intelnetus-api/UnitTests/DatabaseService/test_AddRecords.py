from unittest.mock import Mock, patch

# FUNCTIONS USED
def get_db_mock_connection_and_cursor():
    connection = Mock()
    cursor = connection.cursor()

    return connection, cursor



# UNDER TEST FUNCTIONS
def add_publication(publication_record, connection, cursor):
    query = f"INSERT INTO scopus_publications VALUES('{publication_record.id}', \
            '{publication_record.doi}','{publication_record.year}','{publication_record.title}',\
            '{publication_record.journal}','{publication_record.abstract}','{publication_record.keywords}',\
            '{publication_record.fields}','{publication_record.fields_abbreviations}',{publication_record.citations_count},\
            {publication_record.authors_number},{publication_record.affiliations_number});"
                    
    cursor.execute(query)
    connection.commit()


def add_author(author_record, connection, cursor):
    query = f"INSERT INTO scopus_authors VALUES('{author_record.id}','{author_record.scopus_id}',\
            '{author_record.orcid_id}','{author_record.first_name}','{author_record.last_name}','{author_record.fields_of_study}',\
            '{author_record.affiliations}',{author_record.h_index},{author_record.citations_count});"
    
    cursor.execute(query)
    connection.commit()


def add_organization(organization_record, connection, cursor):
    query = f"INSERT INTO scopus_organizations VALUES('{organization_record.id}',\
            '{organization_record.scopus_id}','{organization_record.name}','{organization_record.type_1}',\
            '{organization_record.type_2}','{organization_record.address}','{organization_record.city}',\
            '{organization_record.country}');"
    
    cursor.execute(query)
    connection.commit()



# TESTS
def test_add_publication():

    mock_connection, mock_cursor = get_db_mock_connection_and_cursor()

    class mock_publication_class:
        def __init__(self):
            self.id = "Id"
            self.doi = "Doi"
            self.year = "2023"
            self.title = "Title"
            self.journal = "Journal"
            self.abstract = "Abstract"
            self.keywords = "Keywords"
            self.fields = "Fields"
            self.fields_abbreviations = "Fields Abbreviations"
            self.citations_count = "1"
            self.authors_number = "1"
            self.affiliations_number = "1"

    publication_record = mock_publication_class()

    with patch.object(mock_cursor, "execute") as mock_execute:
        add_publication(publication_record, mock_connection, mock_cursor)
        expected_query = f"INSERT INTO scopus_publications VALUES('{publication_record.id}', \
            '{publication_record.doi}','{publication_record.year}','{publication_record.title}',\
            '{publication_record.journal}','{publication_record.abstract}','{publication_record.keywords}',\
            '{publication_record.fields}','{publication_record.fields_abbreviations}',{publication_record.citations_count},\
            {publication_record.authors_number},{publication_record.affiliations_number});"
        
        mock_execute.assert_called_once_with(expected_query)
        mock_connection.commit.assert_called_once()


def test_add_author():

    mock_connection, mock_cursor = get_db_mock_connection_and_cursor()

    class mock_author_class:
        def __init__(self):
            self.id = "Id"
            self.scopus_id = "Scopus Id"
            self.orcid_id = "ORCID Id"
            self.first_name = "First Name"
            self.last_name = "Last Name"
            self.fields_of_study = "Fields Of Study"
            self.affiliations = "Affiliations"
            self.h_index = "1.0"
            self.citations_count = "1"

    mock_author = mock_author_class()

    with patch.object(mock_cursor, "execute") as mock_execute:
        add_author(mock_author, mock_connection, mock_cursor)
        
        expected_query = f"INSERT INTO scopus_authors VALUES('{mock_author.id}','{mock_author.scopus_id}',\
            '{mock_author.orcid_id}','{mock_author.first_name}','{mock_author.last_name}','{mock_author.fields_of_study}',\
            '{mock_author.affiliations}',{mock_author.h_index},{mock_author.citations_count});"
        
        
        mock_execute.assert_called_once_with(expected_query)
        mock_connection.commit.assert_called_once()


def test_add_organization():

    mock_connection, mock_cursor = get_db_mock_connection_and_cursor()

    class mock_organization_class:
        def __init__(self):
            self.id = "Id"
            self.scopus_id = "Scopus Id"
            self.name = "Name"
            self.type_1 = "Type 1"
            self.type_2 = "Type 2"
            self.address = "Address"
            self.city = "City"
            self.country = "Country"

    mock_organization = mock_organization_class()

    with patch.object(mock_cursor, "execute") as mock_execute:
        add_organization(mock_organization, mock_connection, mock_cursor)

        expected_query = f"INSERT INTO scopus_organizations VALUES('{mock_organization.id}',\
            '{mock_organization.scopus_id}','{mock_organization.name}','{mock_organization.type_1}',\
            '{mock_organization.type_2}','{mock_organization.address}','{mock_organization.city}',\
            '{mock_organization.country}');"
        
        mock_execute.assert_called_once_with(expected_query)
        mock_connection.commit.assert_called_once()