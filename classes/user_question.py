#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'UserQuestion' class."""


class UserQuestion():
    """This class is used to get and treat the question asked by the user."""
    
    def __init__(self, entered_question):
        """This special method is the class constructor."""
        # super(UserQuestion, self).__init__()
        self.entered_question = entered_question # type is str

    def get_splitted(self):
        """
        This method is responsible for splitting
        the entered question into words.
        """
        ## TO DO
        # check if self.entered_question type is str
        # split()
        pass

    def parse(self):
        """
        This method is responsible for parsing the entered question
        into key words, if the question seems appropriate.
        """
        ## TO DO:
        result = ""
        ## split sentence into words
        ## ignore stop words
        ## algo
        ## result = " ".join(key_words)
        return result

    def request_location(self):
        """
        This method is responsible for determining if the question seems
        appropriate. This returns 'True' if yes, 'False' if not.
        """
        ## TO DO
        pass