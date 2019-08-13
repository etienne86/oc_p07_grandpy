#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'BotReply' class."""

import random


class BotReply():
    """This class is used to get and treat the question asked by the user."""
    
    def __init__(self):
        """This special method is the class constructor."""
        super(BotReply, self).__init__()

    def display_map(self):
        """
        This method is responsible for displaying the map.
        """
        ## TO DO
        pass

    def give_answer_first(self):
        """
        This method is responsible for supplying
        the first part of the answer to the user (i.e. the address).
        """
        ## TO DO
        pass

    def give_answer_second(self):
        """
        This method is responsible for supplying
        the second part of the answer to the user (i.e. the wikipedia extract).
        """
        ## TO DO
        pass

    def reject_question(self):
        """
        This method is responsible for replying that
        the question was not understood by the bot.
        """
        message = "Je suis vraiment désolé, mais je n'ai pas compris " +\
            "ta question, malgré mes lunettes, mes appareils auditifs " +\
            "et ma mémoire d'éléphant. Pourrais-tu me préciser l'endroit " +\
            "dont tu souhaites connaître l'adresse ?"
        return message

    def welcome_message(self):
        """
        This method is responsible for saying hello
        when the user loads the page.
        """
        welcome_part_1 = ["Bonjour ", "Coucou ", "Bien le bonjour "]
        welcome_part_2 = ["mon poussin ! ", "mon chou ! ", "mon petit ! "]
        welcome_part_3 = [
            "Dis-moi, en quoi puis-je t'aider ?",
            "Je t'écoute, où souhaites-tu te rendre ?",
            "Raconte-moi où tu veux aller, et je te dirai comment t'y rendre !"
        ]
        message = welcome_part_1[random.randint(0, len(welcome_part_1) - 1)] +\
            welcome_part_2[random.randint(0, len(welcome_part_2) - 1)] +\
            welcome_part_3[random.randint(0, len(welcome_part_3) - 1)]
        return message