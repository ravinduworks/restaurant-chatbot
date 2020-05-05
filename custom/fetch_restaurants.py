""" Program to get top 10 restaurants.

Returns restaurant list based location, cuisine, rating and minimum and
maximum amount provided by users.
"""

from custom import zomatopy
import json

__author__ = 'rboodher@juniper.net'

ZOMATO_APIKEY = "update-zomato-api-key-here"

def fetch_restaurants(loc, cuisine, budget):
    """ Function to get restaurant data.

    Returns: lists of tuples contains name, address, average cost and rating.
    """
    config={ "user_key":ZOMATO_APIKEY}
    zomato = zomatopy.initialize_app(config)
    location_detail = zomato.get_location(loc, 1)
    d1 = json.loads(location_detail)
    lat=d1["location_suggestions"][0]["latitude"]
    lon=d1["location_suggestions"][0]["longitude"]
    cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,
                    'biryani':7,'north indian':50,'south indian':85,
                    'maxican':73, 'american':1
    }

    # To avoid over usage of Zomato API calls, taking max of 1k restaurant list.
    results = zomato.restaurant_search(
                        "", lat, lon, str(cuisines_dict.get(cuisine)), 1000)
    d = json.loads(results)

    # Three price categories
    price_range = {'lesser than 300':{'min': 0, 'max': 300},
    				'between 300 to 700': {'min': 300, 'max': 700},
    				'more than 700': {'min': 700, 'max': 100000},
    		}
    # Get minimum and maximum amount based on user's input
    min = price_range[budget]['min']
    max = price_range[budget]['max']

    response = {}

    if d['results_found'] == 0:
        response= []
    else:
        count = 1
        for restaurant in d['restaurants']:
            # Filter out all the restaurants with min and max amount
            if restaurant['restaurant']['average_cost_for_two'] > min and \
                restaurant['restaurant']['average_cost_for_two'] < max:
                response[count] = dict()
                response[count]['name'] = restaurant['restaurant']['name']
                response[count]['address'] = restaurant['restaurant'] \
                                                ['location']['address']
                response[count]['average_budget_for_two'] = restaurant[ \
                                'restaurant']['average_cost_for_two']
                response[count]['rating'] = restaurant['restaurant'][ \
                                'user_rating']['aggregate_rating']
                count += 1

    # Sort the restaurant list based on user rating.
    response_sorted = sorted(response.items(), key=lambda x: (str(x[1] \
                                                    ['rating'])), reverse=True)

    # Return top 10 restaurants based on user rating from the result
    return response_sorted[:10]
