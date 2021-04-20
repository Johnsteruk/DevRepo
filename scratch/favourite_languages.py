#!/usr/bin/env python3

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print(favorite_languages)
print(favorite_languages['sarah'])
favorite_languages['john'] = 'sql'
favorite_languages['ann'] = 'c++'
person = 'john'
language = favorite_languages[person].title()
print(f"{person.title()}'s favorite language is {language}.")
