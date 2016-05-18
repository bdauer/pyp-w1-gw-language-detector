

"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    
    # input text converted to set
    set_text = set(text.split())

    for language in languages:
        language['set_common_words'] = set(language['common_words'])


    for language in languages:
        language['score'] = len(set_text.intersection(language['set_common_words']))

    # Longest length is the correct language.
    sum = 0
    for language in languages:
        if language['score'] > sum:
            sum = language['score']
    print languages
    
    # Return the name of the language with the best score
    for language in languages:
        if language['score'] == sum:
            return language['name']