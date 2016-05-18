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
    for language in languages:
        language['set_common_words'] = set(language['common_words'])

def generate_score(languages, set_text):
    """
    Add score to each language in languages.
    """
    for language in languages:
        language['score'] = len(set_text.intersection(language['set_common_words']))
    score = get_highest_score(languages)
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
  
def compute_language(languages, score):
    """
    Return name of language with the max score
    """
    for language in languages:
        if language['score'] == score:
            return language['name']
      
def detect_language(text, languages):
    """Returns the detected language of given text."""
    set_text = create_set_from_text(text)
    create_set_common_words(languages)
    language = generate_score(languages, set_text)
    score = get_highest_score(languages)
    language = compute_language(languages, score)
    return language
