#! /usr/bin/env python3
# coding: utf-8

"""This module contains the tests related to the 'Institution' class."""

from unittest.mock import Mock

import pytest
import googlemaps

from oc_p07_grandpy.classes.institution import Institution
from oc_p07_grandpy.classes.institution import ignore_http_tags, shorten_text


# initialization of a function which mocks:
# - two googlemaps returns:
#   _ 'geocode' return for address, latitude, longitude and place_id
#   _ 'place' return for real name
# - the wikipedia return to get the page text
mock_func = Mock()

def setup_function():
    # the mock function returns a dict
    # (with the same keys as in the 'geocode' and 'place' returns)
    mock_func.return_value = {
        "formatted_address": "mock_address",
        "geometry": {
            "location": {
                "lat": "mock_latitude",
                "lng": "mock_longitude"
            }
        },
        "place_id": "mock_place_id",
        "result": {
            "name" : "mock_name"
        },
        "parse": {
            "text": {
                "*": "mock_wiki_text"
            }
        }
    }

def init_for_geocode_tests(monkeypatch):
    """
    This function is used in several tests
    related to the googlemaps 'geoccode' return.
    """
    # the mocking process with the 'monkeypatch' fixture
    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func)
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
    monkeypatch.setattr(Institution, 'get_place_response', mock_func)
    new_inst = Institution("")
    value = new_inst.get_name()
    assert value == "mock_name"

def test_get_place_id(monkeypatch):
    value = init_for_geocode_tests(monkeypatch).get_place_id()
    assert value == "mock_place_id"

def test_get_wiki_summary():
    new_inst = Institution("")
    full_text = new_inst.get_wiki_text()

def test_get_wiki_text(monkeypatch):
    monkeypatch.setattr(Institution, 'get_wiki_response', mock_func)
    new_inst = Institution("")
    value = new_inst.get_wiki_text()
    assert value == "mock_wiki_text"


def test_ignore_http_tags():
    string = "<strong>Hello!</strong> We are <em>glad</em> to see you!"
    simple_string = "Hello! We are glad to see you!"
    assert ignore_http_tags(string) == simple_string

def test_shorten_text_with_short_string():
    string = "12345678. " * 50 + "123"
    assert shorten_text(string) == string

def test_shorten_text_with_long_string():
    string = "12345678. " * 110 + "123"
    shortened_string = "12345678. " * 99 + "12345678."
    assert shorten_text(string) == shortened_string

def test_shorten_text_without_any_dot():
    string = "123456789 " * 110 + "123"
    shortened_string = "123456789 " * 98 + "123456789" + "..." 
    assert shorten_text(string) == shortened_string
