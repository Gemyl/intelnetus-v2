from lib.helpers import get_sql_syntax
    
# TESTS
def test_get_sql_syntax():

    mock_string = 'string\'s'

    expected_string = 'string s'
    actual_string = get_sql_syntax(mock_string)

    assert(expected_string == actual_string)