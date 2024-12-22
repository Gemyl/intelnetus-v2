# UNDER TEST FUNCTIONS
def get_safe_attribute(obj, attribute, attribute_type):
    try:
        if isinstance(obj, dict):
            value = obj.get(attribute)
            if((value == None) & (attribute_type == "number")):
               value = 999999
            elif (obj.get(attribute) == None):
                value = "-"
        else:
            value = getattr(obj, attribute)
            if((value == None) & (attribute_type == "number")):
               value = 999999
            elif (value == None):
                value = "-"

    except (AttributeError, KeyError):
        if attribute_type == "number":
            value = 999999
        else:
            value = "-"
    
    return value

# TESTS
def test_get_safe_attribute_from_empty_object():

    mock_object = {}
    string_attribute = get_safe_attribute(mock_object, 'attribute_1', 'string')
    number_attribute = get_safe_attribute(mock_object, 'attribute_2', 'number')

    assert(string_attribute == '-')
    assert(number_attribute == 999999)