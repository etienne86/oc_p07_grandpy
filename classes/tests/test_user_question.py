#! /usr/bin/env python3
# coding: utf8

"""This module contains the tests related to the 'UserQuestion' class."""

from unittest.mock import Mock

import pytest

from classes.institution import Institution
from classes.user_question import UserQuestion


# initialization of three functions which mock three 'Geocoding API' returns:
# - a dict with 0 result
mock_func_0 = Mock()
mock_func_0.return_value = {"results": [], "status": "ZERO_RESULTS"}
# - a dict with 1 result
mock_func_1 = Mock()
mock_func_1.return_value = {"results": [{"mock_dict"}], "status": "OK"}
# - a dict with several results (e.g. 2 results)
mock_func_2 = Mock()
mock_func_2.return_value = {
    "results": [
        {"first_mock_dict"},
        {"second_mock_dict"}
    ],
    "status": "OK"
}

# nota: analyze() is not tested entirely,
# as it uses methods already tested

def test_ask_complete_question_true():
    """
    The user asks a complete question,
    with at least one key word to determine an address to search.
    """
    sentence = "Comment va-t-on à la poste ?"
    question = UserQuestion(sentence)
    assert question.ask_complete_question() == True

def test_ask_complete_question_false():
    """
    The user does not ask a complete question,
    because there are not key words enough in the sentence.
    # It assumes that the user question has been already parsed.
    """
    sentence = "Comment vas-tu ?"
    question = UserQuestion(sentence)
    assert question.ask_complete_question() == False 

def test_ask_for_location_true_with_one_key_word():
    """The user asks really for an address with one key word."""
    sentence = "Où est la poste ?"
    question = UserQuestion(sentence)
    assert question.ask_for_location() == True

def test_ask_for_location_true_with_one_phrase():
    """The user asks really for an address with one phrase (several words)."""
    sentence = "Pourrais-tu me dire comment aller à la poste s'il te plaît ?"
    question = UserQuestion(sentence)
    assert question.ask_for_location() == True

def test_ask_for_location_false():
    """The user does not ask for an address."""
    sentence = "Au petit déjeuner, j'aime boire du thé."
    question = UserQuestion(sentence)
    assert question.ask_for_location() == False

def test_ask_for_location_false_with_only_one_word():
    """The user does not ask for an address."""
    sentence = "paris"
    question = UserQuestion(sentence)
    assert question.ask_for_location() == False

def test_ask_precise_question_false_zero_result(monkeypatch):
    """The user does not precise the institution clearly,
    and Google Maps returns 0 result."""
    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func_0)
    question = UserQuestion("")
    assert question.ask_precise_question() == False

def test_ask_precise_question_true(monkeypatch):
    """The user precises the institution clearly,
    and Google Maps returns 1 result."""
    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func_1)
    question = UserQuestion("")
    assert question.ask_precise_question() == True

def test_ask_precise_question_false_several_results(monkeypatch):
    """The user does not precise the institution clearly,
    and Google Maps returns several results."""
    monkeypatch.setattr(Institution, 'get_geocode_response', mock_func_2)
    question = UserQuestion("")
    assert question.ask_precise_question() == False

def test_parse():
    """This function is responsible for testing
    the parsing method on several sentences.
    """
    sentences = [
        "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?",
        "",
        "       ",
        "Comment vas-tu ?",
        "Où est la poste ?",
        "Pourrais-tu me dire comment aller à la poste s'il te plaît ?",
        "Hey GrandPy, salut ! Comment vas-tu ? J'aimerais savoir " +\
            "où se trouve la Tour Montparnasse s'il te plaît ?",
        "Je veux aller faire un tour au zoo de Beauval. Il paraît que " +\
            "cet endroit est merveilleux.",
        "Coucou mon vieux, peux-tu me dire où se trouve " +\
            "la poste de Poitiers STP ?",
        "salut grand py bot, est ce que tu connais " +\
            "la basilique de saint maximin",
        "ou est la tour eiffel",
        "ou trouver la cathedrale notre dame",
    ]
    parsed_sentences = [
        "Openclassrooms",
        "",
        "",
        "",
        "Poste",
        "Poste",
        "Tour Montparnasse",
        "Zoo Beauval",
        "Poste Poitiers",
        "Basilique Saint Maximin",
        "Tour Eiffel",
        "Cathedrale Dame",
    ]
    results = []
    for _ in range(len(sentences)):
        question = UserQuestion(sentences.pop(0))
        results.append(question.parse() == parsed_sentences.pop(0))
    assert not (False in results)