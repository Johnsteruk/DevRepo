#!/usr/bin/env python3

#Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name , last_name , age , and city . Print each
#piece of information stored in your dictionary.

person_information = {
    'forename': 'Laura',
    'surname': 'Campbell',
    'age': 42,
    'resides': 'Amsterdam',
}

print(person_information['forename'])
print(person_information['surname'])
print(person_information['age'])
print(person_information['resides'])

#Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number. For even more fun, poll a few
#friends and get some actual data for your program.
fav_nums = {}

fav_nums['john'] = '13'
fav_nums['laura'] = '17'
fav_nums['ann'] = '7'
fav_nums['stephen'] = '3'
fav_nums['stacy'] = '10'

print(f"John's favourite number is : {fav_nums['john']}")
print(f"Laura's favourite number is : {fav_nums['laura']}")
print(f"Ann's favourite number is : {fav_nums['ann']}")
print(f"Stephen's favourite number is : {fav_nums['stephen']}")
print(f"Stacy's favourite number is : {fav_nums['ann']}")

#A Python dictionary can be used to model an actual dictionary.
#However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous
#chapters. Use these words as the keys in your glossary, and store their
#meanings as values.
#• Print each word and its meaning as neatly formatted output. You might
#print the word followed by a colon and then its meaning, or print the word
#on one line and then print its meaning indented on a second line. Use the
#newline character ( \n ) to insert a blank line between each word-meaning
#pair in your output.

dict_words = {
    'Dictionary': 'It is a key value pair list',
    'List': 'It is a fucking list',
    'Python': 'The language it was written in',
    'Loop': 'A loop',
    'If': 'A statement',
}


#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
#up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When
#you’re sure that your loop works, add five more Python terms to your glossary.
#When you run your program again, these new words and meanings should
#automatically be included in the output.
for key, value in fav_nums.items():
    print(key, value)

fav_nums['cruela'] = '101'
fav_nums['steph'] = '5'
fav_nums['carla'] = '9'
fav_nums['bob'] = '29'
fav_nums['alice'] = '2'

for key, value in fav_nums.items():
    print(f"{key}'s favourite number is : {value}")

#Rivers: Make a dictionary containing three major rivers and the country
#each river runs through. One key-value pair might be 'nile': 'egypt' .
#• Use a loop to print a sentence about each river, such as The Nile runs
#through Egypt.
#• Use a loop to print the name of each river included in the dictionary.
#• Use a loop to print the name of each country included in the dictionary.

rivers = {'clyde':'scotland','thames':'england','liffey':'ireland'}
for k, v in rivers.items():
    print(f"The {k.title()} runs through {v.title()}.")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

#Polling: Use the code in favorite_languages.py (page 97).
#• Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.
#• Loop through the list of people who should take the poll. If they have
#already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take
#the poll.
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'laura': 'javascript',
'bob': 'java',
}

candidates = ['john','fred','bob','alice','jen','sarah','edward','phil','laura']

for name in candidates:
    if name in favorite_languages.keys():
        print(f"Thanks {name.title()} for adding your favourite language.")
    else:
        print(f"Hi {name.title()}, please add your favourite language.")


