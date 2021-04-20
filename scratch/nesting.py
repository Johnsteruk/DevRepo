#!/usr/bin/env python3

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
#Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people . Loop through your list of people. As you
#loop through the list, print everything you know about each person.

people = []

person_information = {
    'forename': 'Laura',
    'surname': 'Campbell',
    'age': 42,
    'resides': 'Amsterdam',
}
people.append(person_information)

person_information = {
    'forename': 'John',
    'surname': 'Campbell',
    'age': 51,
    'resides': 'Amsterdam',
}

people.append(person_information)

person_information = {
    'forename': 'Ann',
    'surname': 'Davidson',
    'age': 55,
    'resides': 'Glasgow',
}

people.append(person_information)

person_information = {
    'forename': 'Stephen',
    'surname': 'Davidson',
    'age': 55,
    'resides': 'Glasgow',
}

people.append(person_information)

person_information = {
    'forename': 'Steph',
    'surname': 'Whittaker',
    'age': 75,
    'resides': 'Nairn',
}

people.append(person_information)

print(people)

for person in people:
    name = person['forename'].title() + " " + person['surname'].title()
    age = str(person['age'])
    city = person['resides'].title()
    
    print(name + ", of " + city + ", is " + age + " years old.")