"""This is the entry point of the program."""

from .languages import LANGUAGES

def create_set_from_text(text):
    """
    return a set of the text
    """
    if not isinstance(text, str):
        raise ValueError("text needs to be a string")
    if len(text) < 1:
        raise ValueError("text cannot be null")
    return set(text.split())

def create_set_common_words(languages):
    """
    create set of common words
    """
    if not isinstance(languages, list):
        raise ValueError("languages should be a valid language list of dictionaries")
    for language in languages:
        if 'common_words' not in language.keys():
            raise ValueError("common_words missing from language: {}".format(language) )
    for language in languages:
        language['set_common_words'] = set(language['common_words'])

def generate_score_for_common_words(languages, set_text):
    """
    Add a score to all the languages by taking an intersection
    between languages and set_text
    """
    for language in languages:
        language['score'] = len(set_text.intersection(language['set_common_words']))

def compute_language_with_highest_score(languages):
    """
    Get the language name with the highest 
    score
    """
    score = get_highest_score(languages)
    for language in languages:
        if language['score'] == score:
            return language['name']
            
def get_highest_score(languages):
    """
    Get the highest score from the languages
    """
    sum = 0
    for language in languages:
        if language['score'] > sum:
            sum = language['score']
            return sum     
  
def detect_language(text, languages):
    """Returns the detected language of given text."""
    set_text = create_set_from_text(text)
    create_set_common_words(languages)
    generate_score_for_common_words(languages, set_text)
    language = compute_language_with_highest_score(languages)
    return language
