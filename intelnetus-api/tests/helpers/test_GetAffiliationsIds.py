# UNDER TEST FUNCTIONS
def get_affiliations_ids(affiliations):

    if affiliations != None:
        return [affil for affil in affiliations.split(";")]
    else:
        return "-"
    
# TESTS
def test_get_afiliations_ids():

    mock_string = '1;2;3;4'

    expected_list = ['1', '2', '3', '4']
    actual_list = get_affiliations_ids(mock_string)

    assert(expected_list == actual_list)