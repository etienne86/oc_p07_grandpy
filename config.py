import os

class Config(object):
    if os.environ.get("GOOGLE_MAPS_API_KEY") is not None:
        GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")
    else:
        GOOGLE_MAPS_API_KEY = ""