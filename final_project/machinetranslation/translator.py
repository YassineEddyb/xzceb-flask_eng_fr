''' this module is for translating french to english and viceversa'''

from deep_translator import MyMemoryTranslator

# english to french
def english_to_french(english_text):
    '''english to french'''

    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

# french to english
def french_to_english(french_text):
    '''french to english'''

    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
