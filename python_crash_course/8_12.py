#!/usr/bin/env python3
#8-12. Sandwiches: Write a function that accepts a list of items a person wants
#on a sandwich. The function should have one parameter that collects as many
#items as the function call provides, and it should print a summary of the sand-
#wich that’s being ordered. Call the function three times, using a different num-
#ber of arguments each time.
def make_sandwich(*fillings):
    """Print the list of toppings that have been requested."""
    print(fillings)
    
make_sandwich('roast beef')
make_sandwich('ham', 'mustard', 'tomato')
make_sandwich('pastrami','mayonnaise')

#8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
#profile of yourself by calling build_profile() , using your first and last names
#and three other key-value pairs that describe you.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('John', 'Campbell',
location='nairn',
shoe_size='8',
hair='brown')
print(user_profile)

#8-14. Cars: Write a function that stores information about a car in a diction-
#ary. The function should always receive a manufacturer and a model name. It
#should then accept an arbitrary number of keyword arguments. Call the func-
#tion with the required information and two other name-value pairs, such as a
#color or an optional feature. Your function should work for a call like this one:
#car = make_car('subaru', 'outback', color='blue', tow_package=True)
#Print the dictionary that’s returned to make sure all the information was
#stored correctly.
def make_car(manufacturer, model_name, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['manufacturer'] = manufacturer
    user_info['model_name'] = model_name
    return user_info

car_profile = make_car('vauxhall','vectra', colour='grey', capacity='2.2', problem='scrapped')
print(car_profile)
