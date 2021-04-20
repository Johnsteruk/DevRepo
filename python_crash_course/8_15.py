#!/usr/bin/env python3

import john as jn

myList = ['Hello', 'Goodbye','See you later','Adios Amigo']
sent_messages= []
jn.print_message(myList, sent_messages)
jn.show_sent_messages(sent_messages)
print(myList)
print(sent_messages)

def make_car(manufacturer, model_name, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['manufacturer'] = manufacturer
    user_info['model_name'] = model_name
    return user_info

car_profile = jn.make_car('vauxhall','vectra', colour='grey', capacity='2.2', problem='scrapped')
print(car_profile)