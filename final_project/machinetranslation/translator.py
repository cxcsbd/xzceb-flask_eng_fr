''' This file contains function definitions for language translation '''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey  = os.environ['apikey']
url     = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator( apikey )
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url( url )

def english_to_french(english_text):
    '''translates text from English to French'''
    if english_text is None :
        french_text = None
    elif english_text is '' :
        french_text = None
    else:
        french_text = language_translator.translate(
            english_text,
            model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    '''translatest text from French to English'''
    if french_text is None :
        english_text = None
    elif french_text is '' :
        english_text = None
    else:
        english_text = language_translator.translate(
            french_text,
            model_id='fr-en').get_result()
    return english_text


# TESTS
#e_input = 'Hello'
#f_out   = english_to_french( e_input )
#print( f_out.get('translations')[0].get('translation') )
#f_in    = 'Bonjour'
#e_out   = french_to_english ( f_in )
#print( e_out.get('translations')[0].get('translation') )
