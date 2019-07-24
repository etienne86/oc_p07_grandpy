#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'AppMarker' class."""

from app_map import AppMap
from institution import Institution
from point import Point


class AppMarker():
    """
    This class is used to deal with a map marker used by GoogleMaps.
    """
    
    def __init__(self, position, map, title):
        """This special method is the class constructor."""
        super(AppMarker, self).__init__()
        self.position = position # type is <class 'Point'>
        self.map = map # type is <class 'AppMap'>
        self.title = title # type is str
