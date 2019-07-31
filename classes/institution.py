#! /usr/bin/env python3
# coding: utf-8

"""This module mainly contains the 'Institution' class."""

import googlemaps

from oc_p07_grandpy.various.config import Config


class NoResponseError(Exception):
    pass


class Institution():
    """
    This class is used to deal with the establishment/place/monument/other
    searched by the user to get its address.
    """
    
    def __init__(self, entered_name):
        """This special method is the class constructor."""
        super(Institution, self).__init__()
        self.entered_name = entered_name # type is str

    def get_formatted_address(self):
        """
        This method is responsible for getting the
        formatted address from the googlemaps module.
        """
        try:
            return self.get_geocode_response()['formatted_address']
        except NoResponseError:
            return 'not understood so not found'

    def get_geocode_response(self):
        """
        This method is responsible for getting the
        geocode response from the googlemaps module.
        This method returns a dict, or raise an exception.
        """
        gmaps = googlemaps.Client(key=Config.GOOGLE_MAPS_API_KEY)
        geocode_result = gmaps.geocode(self.entered_name)
        if geocode_result:
            return geocode_result[0] # returns the first element of the list
        else:
            raise NoResponseError

    def get_latitude(self):
        """
        This method is responsible for getting the
        latitude from the googlemaps module.
        """
        try:
            return self.get_geocode_response()['geometry']['location']['lat']
        except NoResponseError:
            return 'not understood so not found'

    def get_longitude(self):
        """
        This method is responsible for getting the
        longitude from the googlemaps module.
        """
        try:
            return self.get_geocode_response()['geometry']['location']['lng']
        except NoResponseError:
            return 'not understood so not found'

    def get_standard_name(self):
        """
        This method is responsible for getting the standard name,
        based on the name entered by the user.
        """
        result = ""
        return result

    def get_wiki_response(self):
        """
        This method is responsible for getting the
        response from the wikipedia API.
        """
   
    def get_wiki_summary(self):
        """
        This method is responsible for extracting a few sentences
        from the wikipedia page dedicated to the institution.
        """
        result = ""
        return result        
