#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'AppMap' class."""


class AppMap():
    """
    This class is used to deal with a map supplied by GoogleMaps.
    """
    
    def __init__(self, marker, zoom=15):
        """This special method is the class constructor."""
        super(AppMap, self).__init__()
        self.marker = marker # type is <class 'AppMarker'>
        self.zoom = zoom # type is int
