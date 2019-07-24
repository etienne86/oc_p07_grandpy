#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Institution' class."""

import googlemaps


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
        # result = ""
        return result

    def get_latitude(self):
        """
        This method is responsible for getting the
        latitude from the googlemaps module.
        """
        # result = 0.0
        return result

    def get_longitude(self):
        """
        This method is responsible for getting the
        longitude from the googlemaps module.
        """
        # result = 0.0
        return result

    def get_standard_name(self):
        """
        This method is responsible for getting the standard name,
        based on the name entered by the user.
        """
        # result = ""
        return result
   
    def get_wiki_summary(self):
        """
        This method is responsible for extracting a few sentences
        from the wikipedia page dedicated to the institution.
        """
        # result = ""
        return result        
