import pytest

def test_lookup_by_name(phonebook):
  phonebook.add("bob", "1234")
  assert "1234" == phonebook.lookup("bob")

def test_phonebook_contains_all_names(phonebook):
  phonebook.add("bob", "1234")
  assert 'bob' in phonebook.names()

def test_missing_name_raises_error(phonebook):
  with pytest.raises(KeyError):
    phonebook.lookup('bob')