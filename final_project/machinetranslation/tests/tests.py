import unittest
from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('hello'), 'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
