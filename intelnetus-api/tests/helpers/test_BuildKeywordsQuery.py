# UNDER TEST FUNCTIONS
def build_keywords_query(keywords, booleans):

    keywords_list = '('
    for i in range(len(keywords)):
        if i == len(keywords)-1:
            keywords_list = keywords_list + '{' + keywords[i] + '}'
        else:
            keywords_list = keywords_list + '{' + keywords[i] + '} ' + booleans[i] + ' '

    keywords_list = keywords_list + ')'
    keywords = keywords_list
    
    return keywords

# TESTS
def test_build_keywords_query():

    mock_keywords = ['keyword_1', 'keyword_2', 'keyword_3', 'keyword_4']
    mock_booleans = ['AND', 'OR', 'AND NOT']

    expected_keywords_query = '({keyword_1} AND {keyword_2} OR {keyword_3} AND NOT {keyword_4})'
    actual_keywords_query = build_keywords_query(mock_keywords, mock_booleans)

    assert(expected_keywords_query == actual_keywords_query)