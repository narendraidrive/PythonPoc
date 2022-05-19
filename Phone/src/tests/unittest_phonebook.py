from phonebook import Phonebook
import unittest

class PhonebookTest(unittest.TestCase):
    def test_lookup_entry_by_name(self):
        pbk = Phonebook()
        pbk.add('naren', '12345')
        self.assertEqual('12345', pbk.lookup('naren'))

    def test_missing_entry_raises_key_error(self):
        pbk = Phonebook()
        self.assertRaises(KeyError, pbk.lookup, 'missing')

    def test_is_consistent(self):
        pbk = Phonebook()
        self.assertTrue(pbk.is_consistent())
        pbk.add('naren', '12345')
        self.assertTrue(pbk.is_consistent())
        pbk.add('idrive', '01234')
        self.assertTrue(pbk.is_consistent())
        pbk.add('naren1', '12345')
        self.assertFalse(pbk.is_consistent())
        pbk.add('naren2', '123') 
        self.assertFalse(pbk.is_consistent())
    
    def test_phonebook_adds_names_and_numbers(self):
        pbk = Phonebook()
        pbk.add('Sue', '12345')
        self.assertIn('Sue', pbk.get_names())
        self.assertIn('12345', pbk.lookup('Sue'))