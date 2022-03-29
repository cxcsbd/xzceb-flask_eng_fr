
import unittest


class Test_E2F(unittest.TestCase):
    def test1(self):
        self.assertEqual( english_to_french( None ), None)
        self.assertEqual( english_to_french( '' ), None)
        e2f = english_to_french('Hello').get('translations')[0].get('translation')
        self.assertEqual( e2f , 'Bonjour')
        self.assertNotEqual( e2f , 'Hello')

class Test_F2E(unittest.TestCase):
    def test2(self):
        self.assertEqual( french_to_english( None ), None)
        self.assertEqual( french_to_english( '' ), None)
        f2e = french_to_english('Bonjour').get('translations')[0].get('translation')
        self.assertEqual( f2e , 'Hello')
        self.assertNotEqual( f2e , 'Bonjour')

unittest.main()

