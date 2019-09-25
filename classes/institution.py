#! /usr/bin/env python3
# coding: utf8

"""This module mainly contains the 'Institution' class."""

import re

import requests

from various.config import Config


class NoResponseError(Exception):
    pass

class NotFoundError(Exception):
    pass


class Institution():
    """
    This class is used to deal with the establishment/place/monument/other
    searched by the user to get its address.
    """
    
    def __init__(self, entered_name):
        """Build an institution, based on the 'entered_name'."""
        super(Institution, self).__init__()
        self.entered_name = entered_name # type is str

    def get_formatted_address(self):
        """
        This method is responsible for getting the
        formatted address from the googlemaps API.
        This method returns a 'str' value.
        """
        try:
            results = self.get_geocode_response()["results"]
            return results[0]['formatted_address']
        except KeyError:
            return 'key error'
        except IndexError:
            return 'index error'
        except NoResponseError:
            return 'not understood so not found'

    def get_geocode_response(self):
        """
        This method is responsible for getting the
        geocode response from the googlemaps API.
        This method returns a 'list' value, or raise an exception.
        """
        # execute the HTTP request
        geocode_response_http = requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json?"\
                + "address=" + self.entered_name\
                + "&key=" + Config.GOOGLE_MAPS_API_KEY
                + "&language=fr"
        )
        geocode_response_dict = geocode_response_http.json() # type is dict
        # analyze and treat the HTTP response
        if geocode_response_http.status_code == 200:
            return geocode_response_dict
        else:
            raise NoResponseError

    def get_latitude(self):
        """
        This method is responsible for getting the
        latitude from the googlemaps API.
        This method returns a 'float' value.
        """
        try:
            results = self.get_geocode_response()["results"]
            return results[0]['geometry']['location']['lat']
        except NoResponseError:
            return 'not understood so not found'

    def get_longitude(self):
        """
        This method is responsible for getting the
        longitude from the googlemaps API.
        This method returns a 'float' value.
        """
        try:
            results = self.get_geocode_response()["results"]
            return results[0]['geometry']['location']['lng']
        except NoResponseError:
            return 'not understood so not found'

    def get_name(self):
        """
        This method is responsible for getting the 'real' name,
        based on the name entered by the user (and possibly mistyped).
        This method returns a 'str' value.
        """
        try:
            return self.get_place_response()['result']['name']
        except NoResponseError:
            return 'not understood so not found'

    def get_place_id(self):
        """
        This method is responsible for getting the
        place_id from the googlemaps API.
        This method returns a 'str' value.
        """
        try:
            return self.get_geocode_response()["results"][0]['place_id']
        except NoResponseError:
            return 'not understood so not found'

    def get_place_response(self):
        """
        This method is responsible for getting the
        place response from the googlemaps API.
        This method returns a 'dict' value, or raise an exception.
        """
        # execute the HTTP request
        place_response_http = requests.get(
            "https://maps.googleapis.com/maps/api/place/details/json?"\
                + "placeid=" + self.get_place_id()\
                + "&fields=name&key=" + Config.GOOGLE_MAPS_API_KEY
                + "&language=fr"
        )
        place_response_dict = place_response_http.json() # type is dict
        # analyze and treat the HTTP response
        if (place_response_http.status_code == 200) \
                and (place_response_dict["status"] == "OK"):
            return place_response_dict
        else:
            raise NoResponseError

    def get_wiki_response(self):
        """
        This method is responsible for getting the
        response from the wikipedia API.
        This method returns a 'dict' value, or raise an exception.
        """
        # arrange the name for the wikipedia API
        wiki_name = "_".join(self.get_name().split())
        # execute the HTTP request
        wiki_response_http = requests.get(
            "https://fr.wikipedia.org/w/api.php?"\
                + "action=parse&prop=text&format=json"\
                + "&page=" + wiki_name
        )
        wiki_response_dict = wiki_response_http.json() # type is dict
        # analyze and treat the HTTP response
        if wiki_response_http.status_code == 200:
            return wiki_response_dict
        else:
            raise NoResponseError
   
    def get_wiki_summary(self):
        """
        This method is responsible for extracting only a few sentences
        from the wikipedia page text (got by the 'get_wiki_text' method).
        This method returns a 'str' value.
        """
        # identify the correct section, which is after the following flag
        flag = "class=\"mw-headline\""
        splitted_text = self.get_wiki_text().split(flag)
        # some sections are exceptions to be ignored
        exceptions = [
            "(.*)<div class=\"geobox\"(.*)", 
            "(.*)<div class=\"infobox(.*)"
        ]
        # loop on the sections
        n = 1
        returned = False
        while n < len(splitted_text):
            # do not match the focused string with the exceptions
            if (re.match(exceptions[0], splitted_text[n]) is None)\
                    and (re.match(exceptions[1], splitted_text[n]) is None)\
                    and "<p>" in splitted_text[n]: # need <p> inside section
                # get the content between the firsts <p> and </p>
                temp_string = splitted_text[n].split("<p>")[1] # after '<p>'
                temp_string = temp_string.split("</p>")[0] # before '</p>'
                # clean the text
                temp_string = ignore_http_tags(temp_string)
                # decode the text
                temp_string = ignore_codes_and_hooks(temp_string)
                # shorten the text, if necessary
                result = shorten_text(temp_string)
                # indicate that the method will return a 'str' value
                returned = True
                return result
            else:
                n += 1
        if not returned:
            # raise NotFoundError
            return ""

    def get_wiki_text(self):
        """
        This method is responsible for extracting the text
        from the wikipedia page dedicated to the institution.
        This method returns a 'str' value.
        """
        try:
            return self.get_wiki_response()['parse']['text']['*']
        except KeyError:
            return "Enfin, j'en connaissais un rayon... j'ai un peu oublié !"


# sub function used in the method get_wiki_summary()
def ignore_codes_and_hooks(string):
    """
    This function returns the given string, without:
    - some codes (from encoding)
    - the hooks
    """
    # ignore codes
    codes = {"&#160;": ""}
    for key in codes:
        intermediate_result = string.replace(key, codes[key])
    # ignore hooks
    result = ""
    regex = r"\[.*?\]" # regular expression for text inside hooks
    # keep only what is not inside hooks
    result_list = re.split(regex, intermediate_result)
    # concatenate all elements
    for sub in result_list:
        result += sub
    return result

# sub function used in the method get_wiki_summary()
def ignore_http_tags(string):
    """
    This function returns the given string, without the http tags.
    """
    result = ""
    regex = r"<.*?>" # regular expression for an http tag
    # keep only what is not http tags
    result_list = re.split(regex, string)
    # concatenate all elements
    for sub in result_list:
        result += sub
    return result

# sub function used in the method get_wiki_summary()
def shorten_text(string):
    """
    This function returns the given string, shortened to max 1000 characters.
    """
    result = string
    if len(string) > 1000:
        # cut to 1000 characters
        result = string[:999]
        # find the last index of "."
        ind = result.rfind(".")
        # cut properly
        if ind != -1: # at least one occurence of "." is found
            # cut at the end of a sentence
            result = result[:ind + 1]
        else: # no "." is found among 1000 first characters
            space_ind = result.rfind(" ")
            # cut at the end of a word
            result = result[:space_ind] + "..."
    return result
