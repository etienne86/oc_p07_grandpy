#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'BotReply' class."""


class BotReply():
    """This class is used to get and treat the question asked by the user."""
    
    def __init__(self, answer):
        """This special method is the class constructor."""
        super(BotReply, self).__init__()
        self.answer = answer # type is str

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
        pass

    def give_answer_second(self):
        """
        This method is responsible for supplying
        the second part of the answer to the user (i.e. the wikipedia extract).
        """
        pass

    def reject_question(self):
        """
        This method is responsible for replying that
        the question was not understood by the bot.
        """
        pass
