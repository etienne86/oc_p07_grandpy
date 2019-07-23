import googlemaps
from config import Config

gmaps = googlemaps.Client(key=Config.GOOGLE_MAPS_API_KEY)
# Geocoding an institution
geocode_result = gmaps.geocode('tour eifffel')

print(geocode_result)
