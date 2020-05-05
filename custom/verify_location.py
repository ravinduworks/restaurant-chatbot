import json
import inspect
import os

from custom import zomatopy

ZOMATO_APIKEY = "update-zomato-api-key-here"

# Get absolute path of current directory
MY_DIR = os.path.dirname(os.path.abspath(
    inspect.getsourcefile(inspect.currentframe())))

# File which which contains tier 1 and tier 2 cities
FILENAME = 'locations.txt'

def get_city_list(filename):
    """ Read data from file.

    return: list
    """
    supported_city_list = list()
    with open(filename, 'r') as fh:
        for city in fh:
            city = city.strip().lower()
            supported_city_list.append(city)
    return supported_city_list

def verify_location(loc):
    """ Function to verify tier 1 and tier 2 cities.

    returns dictionary.
    """
    supported_city_list = get_city_list(os.path.join(MY_DIR, FILENAME))

    config={"user_key":ZOMATO_APIKEY}
    zomato = zomatopy.initialize_app(config)
    location_detail=zomato.get_location(loc, 1)
    location_json = json.loads(location_detail)
    location_results = len(location_json['location_suggestions'])

    if location_results == 0 or loc.lower() not in supported_city_list:
        return {'location_f' : 'notfound', 'location_new' : None}

    return {'location_f' : 'found', 'location_new' : loc}
