#! /usr/bin/env python3
# coding: utf-8

"""This module contains the tests related to the 'Institution' class."""

from unittest.mock import Mock

import pytest
import googlemaps

import oc_p07_grandpy.classes.institution as institution
from institution import Institution


# def setup_function():
#     gmaps = googlemaps.Client(key=institution.Config.GOOGLE_MAPS_API_KEY)
    

def test_get_formatted_address(monkeypatch):
    
    # a function which mocks the googlemaps 'geocode' return
    mock_func = Mock()
    mock_func.return_value = {"formatted_address": "mock_value"}

    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func)
    new_inst = Institution("")
    value = new_inst.get_formatted_address()
    assert value == "mock_value"


