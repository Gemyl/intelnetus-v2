# UNDER TEST FUNCTIONS
def get_sql_syntax(string):

    if string != None:
        return string.replace("\'", " ")
    else:
        return "-"
    
# TESTS
def test_get_sql_syntax():

    mock_string = 'string\'s'

    expected_string = 'string s'
    actual_string = get_sql_syntax(mock_string)

    assert(expected_string == actual_string)