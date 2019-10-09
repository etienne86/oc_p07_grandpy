#! /usr/bin/env python3
# coding: utf8

"""This module contains the 'UserQuestion' class."""

import re


from classes.institution import Institution, NoResponseError
import data.stop_words as stop_words


class UserQuestion():
    """This class is used to get and treat the question asked by the user."""
    
    def __init__(self, entered_question):
        """Build a user question, based on the 'entered_question'."""
        super(UserQuestion, self).__init__()
        self.entered_question = entered_question # type is str

    def analyze(self, bot):
        """
        This method is responsible for analyzing the user question,
        and calls other methods.
        This returns a dict to feed the bot reply.
        """
        result = {
            'acceptable_question': False,
            'question': "",
            'ask_for_something': ""
        }
        # is this a question to request an address?
        if self.ask_for_location():
            # parse the user question
            result['question'] = self.parse()
            # is the question complete enough?
            if self.ask_complete_question():
                # googlemaps request
                inst = Institution(self.parse())
                try:
                    geo_results = inst.get_geocode_response()["results"]
                    geo_results[0]['formatted_address']
                except NoResponseError:
                    print('not found but captured')
                except IndexError:
                    print('index error')
                # is the question precise enough?
                if self.ask_precise_question():
                    # the question is acceptable
                    result['acceptable_question'] = True
                else:
                    result['ask_for_something'] = bot.ask_for_precision()
            else:
                result['ask_for_something'] = bot.ask_for_completion()
        else:
            result['ask_for_something'] = bot.ask_for_understanding()
        return result

    def ask_complete_question(self):
        """
        This method is responsible for determining
        if the question is complete enough.
        This returns 'True' if yes, 'False' if not.
        """
        if self.parse() is "":
            return False
        else:
            return True

    def ask_for_location(self):
        """
        This method is responsible for determining
        if the question seems appropriate to ask for an address.
        This returns 'True' if yes, 'False' if not.
        """
        key_words = [
            "adresse", "aimerai all", "aimerais all", "cherche",
            "comment all", "comment va", "localis", " me rendre ", "ou ",
            "où ", " se rendre ", "souhaite all", "souhaiterai all",
            "souhaiterais all", "veux aller", "voudrai aller", "voudrais aller"
        ]
        result = False
        while key_words and not result:
            if key_words.pop(0) in self.entered_question.lower():
                result = True
        return result                    

    def ask_precise_question(self):
        """
        This method is responsible for determining
        if the question is precise enough.
        The question is considered as precise if there is one,
        and only one result returned by Google Maps.
        This returns 'True' if yes, 'False' if not.
        """
        inst = Institution(self.parse())
        try:
            length = len(inst.get_geocode_response()["results"])
            if length == 1:
                return True
            else:
                return False
        except NoResponseError:
            return False

    def parse(self):
        """
        This method is responsible for parsing the entered question
        into key words, if the question seems appropriate.
        """
        if self.entered_question == "":
            return ""
        else:
            # remove punctuation
            string = re.sub(r"([,\?;\.\:!/\\\*\(\)\[\]])*",
                            "",
                            self.entered_question)
            # remove apostrophes
            string = string.replace("\'", " ")
            # remove quotation marks
            string = string.replace("\"", " ")
            # remove redundant spaces
            string = re.sub(r"( ){2,}", " ", string)
            # transform to lowercase
            string = string.lower()
            # split
            words_list = string.split()
            # exclude stop words
            limited_list = [word for word in words_list \
                if word not in stop_words.all_fr]
            # exclude stop expressions (two consecutive words)
            lower_result = exclude_expressions(limited_list)
            # capitalize for Google Maps and Wikipedia search
            capitalized_result = [word.capitalize() for word in lower_result]
            return " ".join(capitalized_result)

# sub function used in the method parse()
def exclude_expressions(words):
    """
    This function excludes some expressions from parsing.
    """
    result = words # type is list
    consec = stop_words.consecutive_fr
    for i in range(len(words) - 1):
        for j in range(len(consec)):
            if words[i] == consec[j][0] and words[i+1] == consec[j][1]:
                # remove the two consecutive words
                if i == 0 and i+1 == len(words) - 1: # if list is only two words
                    result = []
                elif i == 0: # if words are at the beginning
                    result = words[i+2:] # keep only the end
                elif i+1 == len(words) - 1: # if words are at the end
                    result = result[:i]
                else:
                    result = result[:i] + words[i+2:]
    return result