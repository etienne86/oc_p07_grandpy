#! /usr/bin/env python3
# coding: utf-8

"""This module contains the tests related to the 'Institution' class."""

from unittest.mock import Mock

import pytest
import googlemaps

import oc_p07_grandpy.classes.institution as institution
from institution import Institution


# class TestInstitution():

mock_func = Mock()

def setup_function():
    # a function which mocks the googlemaps 'geocode' return
    mock_func.return_value = {
        "formatted_address": "mock_address",
        "geometry": {
            "location": {
                "lat": "mock_latitude",
                "lng": "mock_longitude"
            }
        }
    }
    
def test_get_formatted_address(monkeypatch):
    # the mocking process with the 'monkeypatch' fixture
    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func)
    new_inst = Institution("")
    value = new_inst.get_formatted_address()
    assert value == "mock_address"


def test_get_latitude(monkeypatch):
    # the mocking process with the 'monkeypatch' fixture
    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func)
    new_inst = Institution("")
    value = new_inst.get_latitude()
    assert value == "mock_latitude"

def test_get_longitude(monkeypatch):
    # the mocking process with the 'monkeypatch' fixture
    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func)
    new_inst = Institution("")
    value = new_inst.get_longitude()
    assert value == "mock_longitude"