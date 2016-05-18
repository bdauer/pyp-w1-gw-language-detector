# -*- coding: utf-8 -*-
import unittest

from language_detector import *

class TestLanguageDetector(unittest.TestCase):

    def setUp(self):
        self.languages = [
            {
                'name': 'Spanish',
                'common_words': [
                    'el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'ser', 'se',
                    'no', 'haber', 'por', 'con', 'su', 'para', 'como', 'estar',
                    'tener', 'le', 'lo', 'lo', 'todo', 'pero', 'más', 'hacer',
                    'o', 'poder', 'decir', 'este', 'ir', 'otro', 'ese', 'la',
                    'si', 'me', 'ya', 'ver', 'porque', 'dar', 'cuando', 'él',
                    'muy', 'sin', 'vez', 'mucho', 'saber', 'qué', 'sobre',
                    'mi', 'alguno', 'mismo', 'yo', 'también', 'hasta'
                ]
            },
            {
                'name': 'German',
                'common_words': [
                    'das', 'ist', 'du', 'ich', 'nicht', 'die', 'es', 'und',
                    'der', 'was', 'wir', 'zu', 'ein', 'er', 'in', 'sie', 'mir',
                    'mit', 'ja', 'wie', 'den', 'auf', 'mich', 'dass', 'so',
                    'hier', 'eine', 'wenn', 'hat', 'all', 'sind', 'von',
                    'dich', 'war', 'haben', 'für', 'an', 'habe', 'da', 'nein',
                    'bin', 'noch', 'dir', 'uns', 'sich', 'nur',
                    'einen', 'kann', 'dem'
                ]
            }
        ]

    def test_detect_language_spanish(self):
        text = """
            Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
            conocido como Leo Messi, es un futbolista argentino11 que juega
            como delantero en el Fútbol Club Barcelona y en la selección
            argentina, de la que es capitán. Considerado con frecuencia el
            mejor jugador del mundo y calificado en el ámbito deportivo como el
            más grande de todos los tiempos, Messi es el único futbolista en la
            historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
            ellos en forma consecutiva– y el primero en
            recibir tres Botas de Oro.
        """
        result = detect_language(text, self.languages)
        self.assertEqual(result, 'Spanish')

    def test_detect_language_german(self):
        text = """
            Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
            Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
            der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
            erzielte. Inzwischen hat Messi als einziger Spieler mehr als 300
            Erstligatore erzielt und ist damit Rekordtorschütze
            der Primera División.
        """
        result = detect_language(text, self.languages)
        self.assertEqual(result, 'German')

    def test_detect_language_mixed_languages(self):
        text = """
            # spanish
            Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
            conocido como Leo Messi, es un futbolista argentino11 que juega
            como delantero en el Fútbol Club Barcelona y en la selección
            argentina, de la que es capitán.

            # german
            Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
            Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
            der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
            erzielte.
        """
        result = detect_language(text, self.languages)
        self.assertEqual(result, 'Spanish')
    
    def test_create_set_from_text(self):
        text = "I am a very very good boy"
        self.assertEqual(create_set_from_text(text), set(['I', 'am', 'a', 'very', 'good', 'boy']))

    def test_create_set_from_text_null_string(self):
        self.assertRaises(ValueError, create_set_from_text, "")

    def test_create_set_from_text_non_string(self):
        self.assertRaises(ValueError, create_set_from_text, False)
        self.assertRaises(ValueError, create_set_from_text, 2)
    
    def test_create_set_common_words(self):
        test_languages = self.languages[:]
        for language in test_languages:
            language['set_common_words'] = set(language['common_words'])
        create_set_common_words(self.languages)
        self.assertEqual(self.languages, test_languages)

    def test_create_set_common_words_invalid_input(self):
        self.assertRaises(ValueError, create_set_common_words, "Hey There")

    def test_create_set_common_words_invalid_dictionary(self):
        test_dictionary = {
                'foo': 'bar', 
                'rmotr' : 'rocks'}
        self.assertRaises(ValueError, create_set_common_words, test_dictionary )

    def test_generate_score_for_common_words(self):
        test_languages = [
                {
                    'name': 'English', 
                    'common_words': ['I', 'am', 'a', 'hero'],
                    'set_common_words': set(['I', 'am', 'a', 'hero'])}, 
                {
                    'name': 'French', 
                    'common_words': ['gre', 'more', 'blah'], 
                    'set_common_words': set(['gre', 'more', 'blah'])
                    }]
        test_languages_output = test_languages[:]
        text = set("I am a superhero going after world domination".split())
        test_languages_output[0]['score'] = 3
        test_languages_output[1]['score'] = 0
        generate_score_for_common_words(test_languages, text)
        self.assertEqual(test_languages, test_languages_output)

    def test_get_highest_score(self):
        test_languages = [
                {
                    'name': 'English', 
                    'common_words': ['I', 'am', 'a', 'hero'],
                    'set_common_words': set(['I', 'am', 'a', 'hero']),
                    'score': 3}, 
                {
                    'name': 'French', 
                    'common_words': ['gre', 'more', 'blah'], 
                    'set_common_words': set(['gre', 'more', 'blah']),
                    'score': 0
                    }]
        self.assertEqual(get_highest_score(test_languages), 3)

    def test_compute_language_with_highest_score(self):
        test_languages = [
                {
                    'name': 'English', 
                    'common_words': ['I', 'am', 'a', 'hero'],
                    'set_common_words': set(['I', 'am', 'a', 'hero']),
                    'score': 3}, 
                {
                    'name': 'French', 
                    'common_words': ['gre', 'more', 'blah'], 
                    'set_common_words': set(['gre', 'more', 'blah']),
                    'score': 0
                    }]
        self.assertEqual(compute_language_with_highest_score(test_languages), 'English')

