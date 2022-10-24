from geopy.geocoders import Nominatim
import geocoder
from time import sleep


def detect_position():
    # initialize the Nominatim object
    Nomi_locator = Nominatim(user_agent="My App")
    my_location = geocoder.ip('me')
    # my latitude and longitude coordinates
    latitude = my_location.geojson['features'][0]['properties']['lat']
    longitude = my_location.geojson['features'][0]['properties']['lng']
    # get the location
    location = Nomi_locator.reverse(f"{latitude}, {longitude}")
    return location


if __name__ == "__main__":
    sleep(0.00001)
