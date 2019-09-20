#! /usr/bin/env python3
# coding: utf8

"""This module contains the 'AppMap' class."""


class AppMap():
    """
    This class is used to deal with a map supplied by GoogleMaps.
    """
    
    def __init__(self, lat, lng, title="C'est ici !", zoom=15):
        """This special method is the class constructor."""
        super(AppMap, self).__init__()
        self.lat = lat # type is float
        self.lng = lng # type is float       
        self.title = title # type is str
        self.zoom = zoom # type is int
