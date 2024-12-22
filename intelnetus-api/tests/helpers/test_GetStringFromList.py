# UNDER TEST FUNCTIONS
def get_string_from_list(list):

    if list != None:
        string = ', '.join([str(i).lower() for i in list])
    else:
        string = ' '

    return string

# TESTS
def test_get_string_from_list():

    mock_list = ['element_1', 'element_2', 'element_3']
    
    expected_string = 'element_1, element_2, element_3'
    actual_string = get_string_from_list(mock_list)

    assert(expected_string == actual_string)