#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'BotReply' class."""

import random

from classes.app_map import AppMap
from classes.app_marker import AppMarker
from classes.institution import Institution
from classes.point import Point


class BotReply():
    """This class is used to get and treat the question asked by the user."""
    
    def __init__(self):
        """This special method is the class constructor."""
        super(BotReply, self).__init__()
        self.acceptable_question = True

    def ask_for_completion(self):
        """
        This method is responsible for replying that
        the question was not complete enough to determine a location.
        """
        self.acceptable_question = False
        message = "Je suis vraiment désolé, mais je n'ai pas compris " +\
            "ta question, car il me manque des informations concernant " +\
            "ta demande : pourrais-tu la reformuler ? " +\
            "Ainsi, j'espère pouvoir te guider !"
        return message

    def ask_for_precision(self):
        """
        This method is responsible for replying that the question
        was not precise enough to determine a unique location.
        """
        self.acceptable_question = False
        message = "Je suis vraiment désolé, mais je n'ai pas compris " +\
            "ta question, car plusieurs lieux semblent correspondre à ta " +\
            "demande. Pourrais-tu me reposer ta question en précisant " +\
            "davantage l'endroit dont tu souhaites connaître l'adresse ?"
        return message

    def ask_for_understanding(self):
        """
        This method is responsible for replying that
        the sentence was not understood as an address request by the bot.
        """
        self.acceptable_question = False
        message = "Je suis vraiment désolé, mais je n'ai pas compris " +\
            "ta question, malgré mes lunettes, mes appareils auditifs " +\
            "et ma mémoire d'éléphant. Si tu souhaites connaître l'adresse " +\
            "d'un lieu, pourrais-tu reformuler ta demande ?"
        return message

    def give_answer_first(self, inst):
        """
        This method is responsible for supplying
        the first part of the answer to the user (i.e. the address).
        """
        address = inst.get_formatted_address()
        return "Voici l'adresse que tu souhaites :\n" + address

    def give_answer_second(self, inst):
        """
        This method is responsible for supplying
        the second part of the answer to the user (i.e. the wikipedia extract).
        """
        if inst.get_wiki_summary() == "":
            wiki_extr = "Enfin, j'en connaissais un rayon... " +\
                "j'ai un peu oublié !"
        else:
            wiki_extr = inst.get_wiki_summary()
        return "A ce propos, j'en connais un rayon à ce sujet ! " + wiki_extr

    def return_map(self, inst, zoom):
        """
        This method is responsible for returning the map.
        """
        my_point = Point(inst.get_latitude(), inst.get_longitude())
        my_app_marker = AppMarker(position=my_point, title=inst.get_name())
        my_app_map = AppMap(marker=my_app_marker, zoom=zoom)
        return my_app_map

    def welcome_message(self):
        """
        This method is responsible for saying hello
        when the user loads the page.
        """
        welcome_part_1 = ["Bonjour ", "Coucou ", "Bien le bonjour "]
        welcome_part_2 = ["mon poussin ! ", "mon chou ! ", "mon petit ! "]
        welcome_part_3 = [
            "J'ai l'impression que tu cherches une addresse : " +\
                "dis-moi, en quoi puis-je t'aider ?",
            "Je t'écoute, où souhaites-tu te rendre ?",
            "Raconte-moi où tu veux aller, et je te dirai où cela se trouve !"
        ]
        message = welcome_part_1[random.randint(0, len(welcome_part_1) - 1)] +\
            welcome_part_2[random.randint(0, len(welcome_part_2) - 1)] +\
            welcome_part_3[random.randint(0, len(welcome_part_3) - 1)]
        return message