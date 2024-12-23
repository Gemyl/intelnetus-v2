from lib.helpers import get_safe_attribute

# TESTS
def test_get_safe_attribute_from_empty_object():

    mock_object = {}
    string_attribute = get_safe_attribute(mock_object, 'attribute_1', 'string')
    number_attribute = get_safe_attribute(mock_object, 'attribute_2', 'number')

    assert(string_attribute == '-')
    assert(number_attribute == 999999)