from lib.constants import COMMON_WORDS
from lib.helpers import remove_common_words

# TESTS
def test_remove_common_words():

    mock_string = 'best common for I AND you'

    expected_string = "best common"
    actual_string = remove_common_words(mock_string, COMMON_WORDS)

    assert(expected_string == actual_string) 