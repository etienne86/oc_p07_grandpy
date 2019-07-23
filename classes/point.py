#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Point' class."""


class Point():
    """
    This class is used to deal with latitude and longitude.
    """
    
    def __init__(self, lat, lng):
        """This special method is the class constructor."""
        # super(Point, self).__init__()
        self.lat = lat # type is float
        self.lng = lng # type is float
