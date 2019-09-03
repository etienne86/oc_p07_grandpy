#! /usr/bin/env python3
# coding: utf-8

"""This module contains the tests related to the 'BotReply' class."""

from unittest.mock import Mock

import pytest

from classes.bot_reply import BotReply
from classes.institution import Institution


def test_return_map(monkeypatch):
    mock_func_map = Mock()
    # the mock function returns a dict:
    # with the same key as in the 'geocode' return for googlemaps
    mock_func_map.return_value = {
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
        ]
    }
    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func_map)
    bot = BotReply()
    inst = Institution("")
    expected_type = "<class 'classes.app_map.AppMap'>"
    assert str(type(bot.return_map(inst, zoom=10))) == expected_type

def test_give_answer_first(monkeypatch):
    mock_func_1 = Mock()
    # the mock function returns a dict:
    # with the same key as in the 'geocode' return for googlemaps
    mock_func_1.return_value = {
        "results":
            [
                {"formatted_address": "mock_address"}
            ]
    }
    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func_1)
    bot = BotReply()
    inst = Institution("")
    text = "Voici l'adresse que tu souhaites :\nmock_address"
    assert bot.give_answer_first(inst) == text

def test_give_answer_second(monkeypatch):
    mock_func_2 = Mock()
    # the mock function returns a 'str' value
    mock_func_2.return_value = "mock_wiki_summary"
    monkeypatch.setattr(Institution, 'get_wiki_summary', mock_func_2)
    bot = BotReply()
    inst = Institution("")
    text = "A ce propos, j'en connais un rayon à ce sujet ! mock_wiki_summary"
    assert bot.give_answer_second(inst) == text
