# VARIABLES USED
COMMON_WORDS = ['a', 'an', 'the', 'and', 'or', 'but', 'if', 'of', 'at', 'by', 'for', 'with', 'about',
                'to', 'from', 'in', 'on', 'up', 'out', 'as', 'into', 'through', 'over', 'after', 'under',
                'i', 'you', 'he', 'she', 'it', 'we', 'they', 'is', 'are', 'was', 'were', 'has', 'had',
                'will', 'be', 'not', 'would', 'should', 'before', 'few', 'many', 'much', 'so', 'furthermore']

# UNDER TEST FUNCTIONS
def remove_common_words(abstract, common_words):

    abstract_list = abstract.split(" ")
    abstract_string = " ".join(
        [word for word in abstract_list if word.lower() not in common_words])
    
    return abstract_string

# TESTS
def test_remove_common_words():

    mock_string = 'best common for I AND you'

    expected_string = "best common"
    actual_string = remove_common_words(mock_string, COMMON_WORDS)

    assert(expected_string == actual_string) 