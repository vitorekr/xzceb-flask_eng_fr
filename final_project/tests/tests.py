import unittest
from translator import english_to_french, french_to_english

class TestTranslationMethods(unittest.TestCase):
    
    def test_english_to_french(self):
        # Test case 1
        english_text = 'Hello'
        expected_output = 'Bonjour'
        self.assertEqual(english_to_french(english_text), expected_output)
        
        # Test case 2
        english_text = ''
        expected_output = ''
        self.assertEqual(english_to_french(english_text), expected_output)
        
    def test_french_to_english(self):
        # Test case 1
        french_text = 'Bonjour'
        expected_output = 'Hello'
        self.assertEqual(french_to_english(french_text), expected_output)
        
        # Test case 2
        french_text = ''
        expected_output = ''
        self.assertEqual(french_to_english(french_text), expected_output)
        
    def test_translation_hello_bonjour(self):
        # Test case
        english_text = 'Hello'
        expected_output = 'Bonjour'
        self.assertEqual(english_to_french(english_text), expected_output)
        
        # Test case
        french_text = 'Bonjour'
        expected_output = 'Hello'
        self.assertEqual(french_to_english(french_text), expected_output)
        
    def test_translation_bonjour_hello(self):
        # Test case
        french_text = 'Bonjour'
        expected_output = 'Hello'
        self.assertEqual(french_to_english(french_text), expected_output)
        
        # Test case
        english_text = 'Hello'
        expected_output = 'Bonjour'
        self.assertEqual(english_to_french(english_text), expected_output)

if __name__ == '__main__':
    unittest.main()
