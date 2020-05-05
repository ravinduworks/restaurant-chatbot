## full path story
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_check_location
    - slot{"location": "mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## full path with email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## Full path with city not serving
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Allahabad"}
    - action_check_location
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots


## Full path with city not serving american
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Allahabad"}
    - action_check_location
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## Full path with moderate price
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## With misspelled location
* affirm
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## Full path with moderate price maxican
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "maxican"}
    - slot{"cuisine": "maxican"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## Full path no email required
* affirm
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## Full path with email id verification
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Kochi"}
    - action_check_location
    - slot{"location": "Kochi"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email
    - action_send_email
    - slot{"email": null}
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* send_email{"email": "abc@xyz.com"}
    - slot{"email": "abc@xyz.com"}
    - action_send_email
    - reset_slots

## story 1 maxican
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "maxican"}
    - slot{"cuisine": "maxican"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* send_email{"email": "abc@xyz.com"}
    - slot{"email": "abc@xyz.com"}
    - action_send_email
    - reset_slots

## story 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "testmail@gmail.com"}
    - slot{"email": "testmail@gmail.com"}
    - action_send_email
    - reset_slots

## Location None 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolhapur"}
    - slot{"location": "kolhapur"}
    - action_check_location
    - slot{"location": "kolhapur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## location specified 4
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "testmail@gmail.com"}
    - slot{"email": "testmail@gmail.com"}
    - action_send_email
    - reset_slots

## complete path 5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## complete path 6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - action_check_location
    - slot{"location": null}
    - utter_ask_location
    - action_check_location
	  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart


## complete path 7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart


## story 8
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## story 8 maxican
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "maxican"}
    - slot{"cuisine": "maxican"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## story 9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 10
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 9 american
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## happy_path 12
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## Ask Cuisine and no location 13
* greet
    - utter_greet
* restaurant_search{"location": "chenna"}
    - slot{"location": "chenna"}
    - action_check_location
    - slot{"location": null}
    - action_check_location
    - slot{"location": "chennai"}
    - utter_ask_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## Ask Cuisine 14
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - utter_ask_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 15
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 16
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_check_location
    - slot{"location": "mysore"}
    - utter_ask_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 17
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_check_location
    - slot{"location": null}
    - utter_ask_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 18
* greet
    - utter_greet
* restaurant_search{"location": "belgaum"}
    - slot{"location": "belgaum"}
    - action_check_location
    - slot{"location": "belgaum"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "belgaum"}
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email

## story 19
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email

## story 20
* greet
    - utter_greet
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 21
* greet
    - utter_greet
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 22
* greet
    - utter_greet
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 23
* greet
    - utter_greet
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email

## story 24
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 25
* greet
    - utter_greet
* restaurant_search{"price": "more than 700", "location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"price": "more than 700"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 26
* greet
    - utter_greet
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email

## story 17
* greet
    - utter_greet
* restaurant_search{"price": "between 300 to 700", "location": "pune"}
    - slot{"location": "pune"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"price": "between 300 to 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email

## story 28
* greet
    - utter_greet
* restaurant_search{"price": "more than 700", "location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - slot{"price": "more than 700"}
    - action_check_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 29
* greet
    - utter_greet
* restaurant_search{"price": "more than 700", "location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - slot{"price": "more than 700"}
    - action_check_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 30
* greet
    - utter_greet
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 31
* restaurant_search{"price": "between 300 to 700", "location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"price": "between 300 to 700"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 32
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email

## story 33
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_check_location
    - slot{"location": "bangalore"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 34
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 35
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "price": "lesser than 300"}
    - slot{"location": "bangalore"}
    - slot{"price": "lesser than 300"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* affirm
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "testmail@gmail.com"}
    - slot{"email": "testmail@gmail.com"}
    - action_send_email
    - reset_slots

## story 36
* greet
    - utter_greet
* restaurant_search{"location": "noida", "price": "between 300 to 700"}
    - slot{"location": "noida"}
    - slot{"price": "between 300 to 700"}
    - action_check_location
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 37
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## story 38
* greet
    - utter_greet
* restaurant_search{"location": "aurangabad", "price": "more than 700"}
    - slot{"location": "aurangabad"}
    - slot{"price": "more than 700"}
    - action_check_location
    - slot{"location": "aurangabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"location": "aurangabad"}
* affirm
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 39
* greet
    - utter_greet
* restaurant_search{"location": "aurangabad", "price": "lesser than 300", "cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "aurangabad"}
    - slot{"price": "lesser than 300"}
    - action_check_location
    - slot{"location": "aurangabad"}
    - action_search_restaurants
    - slot{"location": "aurangabad"}
* affirm
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 40
* greet
    - utter_greet
* restaurant_search{"location": "aurangabad"}
    - slot{"location": "aurangabad"}
    - action_check_location
    - slot{"location": "aurangabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "aurangabad"}
    - utter_ask_email
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 41
* greet
    - utter_greet
* restaurant_search{"location": "aurangabad"}
    - slot{"location": "aurangabad"}
    - action_check_location
    - slot{"location": "aurangabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "aurangabad"}
* affirm
    - utter_ask_email
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 42
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_check_location
    - slot{"location": "gurgaon"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "gurgaon"}
* affirm
    - utter_ask_email
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 43
* greet
    - utter_greet
* restaurant_search{"price": "lesser than 300", "location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"price": "lesser than 300"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* affirm
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 44
* greet
    - utter_greet
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - action_check_location
    - slot{"location": null}
    - utter_ask_again

## story ask again
* greet
    - utter_greet
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - action_check_location
    - slot{"location": null}
    - utter_ask_again
    - action_check_location
    - slot{"location": null}
    - utter_ask_again
    - action_check_location
    - slot{"location": null}
    - utter_ask_again
    - action_check_location
    - slot{"location": null}
    - utter_ask_again
    - action_check_location
    - slot{"location": null}
    - utter_ask_again
    - action_check_location
    - slot{"location": "mysore"}

## story 45
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 46
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots


## story 47
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 48
* affirm
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 41 fix price > 700
* greet
    - utter_greet
* restaurant_search{"location": "kolkata", "price": "more than 700"}
    - slot{"location": "kolkata"}
    - slot{"price": "more than 700"}
    - action_check_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## Path with moderate price
* restaurant_search{"price": "between 300 to 700", "location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"price": "between 300 to 700"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 49
* greet
    - utter_greet
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_check_location
    - slot{"location": "Kochi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - utter_ask_email
* send_email
    - utter_ask_email_id
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 50
* greet
    - utter_greet
* restaurant_search{"location": "belgaum"}
    - slot{"location": "belgaum"}
    - action_check_location
    - slot{"location": "belgaum"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "belgaum"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## resturant search in unknown location
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "manasasarovara"}
    - slot{"location": "manasasarovara"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "belgaum"}
    - slot{"location": "belgaum"}
    - action_check_location
    - slot{"location": "belgaum"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "belgaum"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 51
* greet
    - utter_greet
* restaurant_search{"location": "davanagere"}
    - slot{"location": "davanagere"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_check_location
    - slot{"location": "mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_email
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## Unknown location and restaurant not found in price range
* greet
    - utter_greet
* unknown{"unknown": "bangaloreeeee"}
    - utter_ask_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"price": null}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"price": null}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## resturant not found in price range and reset slots
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"price": null}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## unknown location and reset slot after email triggered
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"price": null}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## Location unknown
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"unknown": "basavapatna"}
    - slot{"location": "basavapatna"}
    - action_check_location
* restaurant_search{"location": "Amravati"}
    - slot{"location": "Amravati"}
    - action_check_location
    - slot{"location": "Amravati"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"price": null}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Amravati"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_email{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## unknown location and email not required.
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"unknown": "asdigasdg"}
    - utter_ask_again
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_check_location
    - slot{"location": "mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## No greet, direct query
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## misspelled location
* restaurant_search{"unknown": "bangaloreeeee", "price": "lesser than 300", "cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"price": "lesser than 300"}
    - action_check_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## misspelled location
* greet
    - utter_greet
* restaurant_search{"location": "bungaluru"}
    - slot{"location": "bungaluru"}
    - action_check_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
    - action_search_restaurants

## misspelled location and continue conversation
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## noopee
* greet
    - utter_greet
* restaurant_search{"location": "bangaloru"}
    - slot{"location": "bangaloru"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* email_not_required{"email_not_required": "noopee"}
    - utter_email_not_required
    - action_restart

## unknown location
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_check_location
    - slot{"location": "mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## story 52
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## story 53
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 54
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
    - action_search_restaurants

## story 55
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "agra"}
    - utter_ask_email
* restaurant_search{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots

## story 56
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - action_check_location
    - slot{"location": "ajmer"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "ajmer"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## story 57
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "aligarh"}
    - slot{"location": "aligarh"}
    - action_check_location
    - slot{"location": "aligarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "aligarh"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## Fix Bombay location
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* email_not_required
    - utter_email_not_required
    - action_restart

## Fix Bombay location
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* restaurant_search{"email": "customer-email@gmail.com"}
    - slot{"email": "customer-email@gmail.com"}
    - action_send_email
    - reset_slots
