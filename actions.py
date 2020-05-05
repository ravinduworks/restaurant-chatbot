from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
from custom import zomatopy
from custom.verify_location import verify_location
from custom.fetch_restaurants import fetch_restaurants
from custom.send_email import send_foodie_list

import json
import re

results = list()

class ActionSearchRestaurants(Action):
	""" Search restaurants.

	Returns: Top 5 restaurants in a sorted order (descending) of the average
	Zomato user rating
	"""
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):

		global results

		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('price')

		results = fetch_restaurants(loc, cuisine, budget)

		response = ""

		# Top 5 restaurants in a sorted order (desc) of the avg Zomato user rating
		if len(results) == 0:
			dispatcher.utter_message("Sorry, we could not find restaurants in" \
						         " the price range requested, please try some" \
								 " other price: " + "\n")
			return [SlotSet('price', None)]

		for res in results[:5]:
			response = response + res[1]['name'] + ' in ' +  res[1]['address'] \
							+ ' has been rated ' + str(res[1]['rating']) + "\n"

		dispatcher.utter_message("Showing you top rated restaurants: " + "\n" \
								+ response)
		return [SlotSet('location',loc)]

class ActionSearchRestaurants(Action):
	""" Send email.

	Top 10 restaurants in a sorted order (descending) of the average Zomato
	user rating

	return: dict with message
	"""
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):

		email = tracker.get_slot('email')

		# verify if the email is valid
		regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

		if not re.match(regex, str(email)):
			dispatcher.utter_message("Email provided is not valid!" \
									" Please try again.")
			return [SlotSet('email', None)]

		# Send top 10 restaurants list in sorted order highest rated being top.
		send_foodie_list(email, results)
		dispatcher.utter_message("Email has been sent!")
		return [AllSlotsReset()]

class VerifyLocation(Action):
	""" Verify location.

	Check if the location provided is in the list of Tier 1 and Tier 2 cities
	and if it is being served by Zomato.

	return: dict
	"""
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		loc = str(loc)
		verify = verify_location(loc)

		if verify['location_f'] == 'notfound':
			dispatcher.utter_message(text="Sorry we do not operate in this" \
									" area yet. try some other location." \
									+ "\n" + "\n" + "Please retype location" \
									" name if misspelled")
			return[SlotSet('location', None)]

		return [SlotSet('location',verify['location_new'])]
