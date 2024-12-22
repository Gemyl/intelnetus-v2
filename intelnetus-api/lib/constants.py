BLUE = "\033[1;34m"
RESET = "\033[0m"
MAX_COLUMN_SIZE = 5000
ORGANIZATIONS_TYPES_KEYWORDS = {
    "university": ['university', 'college', 'departement'],
    "academy": ['academy', 'academic', 'academia'],
    "school": ['school', 'faculty'],
    "research": ['research', 'researchers'],
    "business": ['inc', 'ltd', 'corporation'],
    "association": ['association'],
    "non-profit": ['non-profit'],
    "government": ['government', 'gov', 'public', 'state', 'national', 'federal', 'federate', 'confederate', 'royal'],
    "international": ['international']
}

SCOPUS_FIELDS = ['AGRI', 'ARTS', 'BIOC', 'BUSI', 'CENG', 'CHEM', 
    'COMP','DECI', 'DENT', 'EART', 'ECON', 'ENER', 'ENGI', 'ENVI',
    'HEAL', 'IMMU', 'MATE', 'MATH', 'MEDI', 'MULT', 'NEUR', 'NURS', 
    'PHAR', 'PHYS', 'PSYC', 'SOCI', 'VETE']

COMMON_WORDS = ['a', 'an', 'the', 'and', 'or', 'but', 'if', 'of', 'at', 'by', 'for', 'with', 'about',
    'to', 'from', 'in', 'on', 'up', 'out', 'as', 'into', 'through', 'over', 'after', 'under',
    'i', 'you', 'he', 'she', 'it', 'we', 'they', 'is', 'are', 'was', 'were', 'has', 'had',
    'will', 'be', 'not', 'would', 'should', 'before', 'few', 'many', 'much', 'so', 'furthermore'] 