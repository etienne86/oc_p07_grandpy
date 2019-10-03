#! /usr/bin/env python3
# coding: utf8

"""This module contains the tests related to the 'Institution' class."""

from unittest.mock import Mock

import pytest

from classes.institution import Institution
from classes.institution import ignore_codes_and_hooks
from classes.institution import ignore_http_tags, shorten_text


# initialization of three functions which mocks:
# - two googlemaps returns:
#   _ 'geocode' return for address, latitude, longitude and place_id
#   _ 'place' return for real name
# - the wikipedia return to get the page text
mock_func_geocode = Mock()
mock_func_place = Mock()
mock_func_wiki = Mock()

def init_for_geocode_tests(monkeypatch):
    """
    This function is used in several tests
    related to the googlemaps 'geocode' return.
    """
    # the mock function returns a list containing a dict,
    # with the same keys as in the 'geocode' return for googlemaps
    mock_func_geocode.return_value = {
        "results": [
            {
                "formatted_address": "mock_address",
                "geometry": {
                    "location": {
                        "lat": "mock_latitude",
                        "lng": "mock_longitude"
                    }
                },
                "place_id": "mock_place_id"
            }
        ],
        "status": "OK"
    }

    # the mocking process with the 'monkeypatch' fixture
    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func_geocode)
    new_inst = Institution("")
    return new_inst

def test_get_formatted_address(monkeypatch):
    value = init_for_geocode_tests(monkeypatch).get_formatted_address()
    assert value == "mock_address"

def test_get_latitude(monkeypatch):
    value = init_for_geocode_tests(monkeypatch).get_latitude()
    assert value == "mock_latitude"

def test_get_longitude(monkeypatch):
    value = init_for_geocode_tests(monkeypatch).get_longitude()
    assert value == "mock_longitude"

def test_get_name(monkeypatch):
    # the mock function returns a dict,
    # with the same keys as in the 'place' return for googlemaps
    mock_func_place.return_value = {
        "result": {
            "name" : "mock_name"
        }
    }
    # the mocking process with the 'monkeypatch' fixture
    monkeypatch.setattr(Institution, 'get_place_response', mock_func_place)
    new_inst = Institution("")
    value = new_inst.get_name()
    assert value == "mock_name"

def test_get_place_id(monkeypatch):
    value = init_for_geocode_tests(monkeypatch).get_place_id()
    assert value == "mock_place_id"


def test_get_wiki_text(monkeypatch):
    # the mock function returns a dict,
    # with the same keys as in the wikipedia return
    mock_func_wiki.return_value = {
        "parse": {
            "text": {
                "*": "mock_wiki_text"
            }
        }
    }
    monkeypatch.setattr(Institution, 'get_wiki_response', mock_func_wiki)
    new_inst = Institution("")
    value = new_inst.get_wiki_text()
    assert value == "mock_wiki_text"

# nota: get_wiki_summary() is not tested directly,
# as it uses methods and functions already tested


def test_ignore_codes_and_hooks_with_only_codes():
    string = "100&#160;km, this is huge!"
    simple_string = "100km, this is huge!"
    assert ignore_codes_and_hooks(string) == simple_string

def test_ignore_codes_and_hooks_with_only_hooks():
    string = "100km[1], this is huge[2]!"
    simple_string = "100km, this is huge!"
    assert ignore_codes_and_hooks(string) == simple_string

def test_ignore_codes_and_hooks_with_both():
    string = "100&#160;km[1], this is huge[2]!"
    simple_string = "100km, this is huge!"
    assert ignore_codes_and_hooks(string) == simple_string

def test_ignore_http_tags():
    string = "<strong>Hello!</strong> We are <em>glad</em> to see you!"
    simple_string = "Hello! We are glad to see you!"
    assert ignore_http_tags(string) == simple_string

def test_shorten_text_with_short_string():
    """The string is short enough, so this stays as it is."""
    string = "12345678. " * 50 + "123"
    assert shorten_text(string) == string

def test_shorten_text_with_long_string():
    """
    The string is long, and this will be shortened at the end of a sentence.
    """
    string = "12345678. " * 110 + "123"
    shortened_string = "12345678. " * 99 + "12345678."
    assert shorten_text(string) == shortened_string

def test_shorten_text_without_any_dot():
    """
    The string is long, and this will be shortened
    before the end of a sentence.
    """
    string = "123456789 " * 110 + "123"
    shortened_string = "123456789 " * 98 + "123456789" + "..." 
    assert shorten_text(string) == shortened_string
