def get_safe_attribute(obj, attribute, attributeType):
    try:
        if isinstance(obj, dict):
            value = obj.get(attribute)
            if((value == None) & (attributeType == "number")):
               value = 999999
            elif (obj.get(attribute) == None):
                value = "-"
        else:
            value = getattr(obj, attribute)
            if((value == None) & (attributeType == "number")):
               value = 999999
            elif (value == None):
                value = "-"

    except (AttributeError, KeyError):
        if attributeType == "number":
            value = 999999
        else:
            value = "-"
    
    return value

        
def build_keywords_query(keywords, booleans):

    keywords_list = '('
    for i in range(len(keywords)):
        if i == len(keywords)-1:
            keywords_list = keywords_list + '{' + keywords[i] + '}'
        else:
            keywords_list = keywords_list + '{' + keywords[i] + '} ' + booleans[i]

    keywords_list = keywords_list + ')'
    keywords = keywords_list

    return keywords


def get_string_from_list(list):

    if list != None:
        string = ', '.join([str(i).lower() for i in list])
    else:
        string = ' '

    return string


def get_sql_syntax(string):

    if string != None:
        return string.replace("\'", " ")
    else:
        return "-"


def remove_common_words(abstract, common_words):

    abstract_list = abstract.split(" ")
    abstract_string = " ".join(
        [word for word in abstract_list if word.lower() not in common_words])
    
    return abstract_string


def get_affiliations_ids(affiliations):

    if affiliations != None:
        return [affil for affil in affiliations.split(";")]
    else:
        return "-"