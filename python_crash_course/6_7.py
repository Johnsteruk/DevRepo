#!/usr/bin/env python3

#6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
#Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people . Loop through your list of people. As you
#loop through the list, print everything you know about each person.

people = []

person = {
    'forename': 'Laura',
    'surname': 'Campbell',
    'age': 42,
    'resides': 'Amsterdam',
}

people.append(person)

person = {
    'forename': 'Stephen',
    'surname': 'Davidson',
    'age': 55,
    'resides': 'Glasgow',
}

people.append(person)

person = {
    'forename': 'Ann',
    'surname': 'Davidson',
    'age': 56,
    'resides': 'Paisley',
}

people.append(person)

for person in people:
    print(f"The persons name is {person['forename'].title()} {person['surname'].title()}")
    print(f"Their age is : {person['age']}")
    print(f"and they live in {person['resides']}.")


#6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
#ent pet. In each dictionary, include the kind of animal and the owner’s name.
#Store these dictionaries in a list called pets . Next, loop through your list and as
#you do, print everything you know about each pet.
pets = []

pet = {
    'owner' : 'John',
    'animal': 'dog',
    'weight': '10 kg',
    'eats' : 'dog food',
    'name' : 'Brandon',
    'colour' : 'black and white'
}

pets.append(pet)

pet = {
    'owner' : 'Laura',
    'animal': 'cat',
    'weight': '5 kg',
    'eats' : 'cat food',
    'name' : 'Zorro',
    'size' : '30cm'
}

pets.append(pet)

pet = {
    'owner' : 'Stacy',
    'animal': 'hamster',
    'weight': '0.5 kg',
    'eats' : 'seeds',
    'name' : 'albert'
}

pets.append(pet)

pet = {
    'owner' : 'Jodie',
    'animal': 'goldfish',
    'weight': '10 grams',
    'eats' : 'fish food',
    'name' : 'hawn'
}

pets.append(pet)

pet = {
    'owner' : 'Ben',
    'animal': 'budgie',
    'weight': '200 grams',
    'eats' : 'trill',
    'name' : 'darth',
    'age' : '3'
}

pets.append(pet)

for pet in pets:
    print(f"Here is all I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))


#6-9. Favorite Places: Make a dictionary called favorite_places . Think of three
#names to use as keys in the dictionary, and store one to three favorite places
#for each person. To make this exercise a bit more interesting, ask some friends
#to name a few of their favorite places. Loop through the dictionary, and print
#each person’s name and their favorite places.
favorite_places = {
    'john': ['nitshill', 'nairn', 'amsterdam', 'fort william'],
    'laura': ['nairn', 'tokyo', 'new york'],
    'ann': ['nitshill', 'paisley', 'wimbledon'],
    'stephen' : ['pollok','possil','manchester']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())

#6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
#so each person can have more than one favorite number. Then print each per-
#son’s name along with their favorite numbers.
favorite_numbers = {
    'john': [42, 17],
    'laura': [17, 3, 12],
    'stephen': [7],
    'ann': [10, 18, 23, 57]
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))



#6-11. Cities: Make a dictionary called cities . Use the names of three cities as
#keys in your dictionary. Create a dictionary of information about each city and
#include the country that the city is in, its approximate population, and one fact
#about that city. The keys for each city’s dictionary should be something like
#country , population , and fact . Print the name of each city and all of the infor-
#mation you have stored about it.

cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
        }
    }

for city, city_info in cities.items():
    print(f"\n {city.title()} is in {city_info['country'].title()}")
    print(f"\tIt has a population of about  {str(city_info['population'])}")
    print(f"\tThe {city_info['nearby mountains'].title()} mountains are nearby.")