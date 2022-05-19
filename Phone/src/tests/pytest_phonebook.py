import pytest
from phonebook import Phonebook


def test_add_and_lookup_entry():
    pbk = Phonebook()
    pytest.skip('WIP')
    pbk.add('Naren', '123')
    assert '123' == pbk.lookup('Naren'), 'Naren not found'


def test_phonebook_gives_access_to_names_and_numbers():
    pbk = Phonebook()
    pbk.add('idrive', '12345')
    assert 'idrive' in pbk.get_names()
    assert '12345' in pbk.get_numbers()


def test_missing_entry_raises_key_error():
    pbk = Phonebook()
    with pytest.raises(KeyError):
        pbk.lookup('missing') 
