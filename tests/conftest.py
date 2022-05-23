"""Shared fixtures"""

import pytest
import requests
from sample.phonebook import Phonebook

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
  "Disable API calls"
  def stunted_get():
    raise RuntimeError("Network access not allowed during testing!")
  monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())

@pytest.fixture
def phonebook(tmpdir):
  "Provides an empty Phonebook"
  return Phonebook(tmpdir)
