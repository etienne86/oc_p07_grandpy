#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'AppMap' class."""

import googlemaps

from point import Point


class AppMap():
    """
    This class is used to deal with a map supplied by GoogleMaps.
    """
    
    def __init__(self, zoom, center):
        """This special method is the class constructor."""
        super(AppMap, self).__init__()
        self.zoom = zoom # type is int
        self.center = center # type is <class 'Point'>
