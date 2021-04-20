#!/usr/bin/env python3

#8-6. City Names: Write a function called city_country() that takes in the name
#of a city and its country. The function should return a string formatted like this:
#"Santiago, Chile"
#Call your function with at least three city-country pairs, and print the
#values that are returned.

def city_country(city, country):
    print(f"{city}, {country}")

city_country('Glasgow', 'Scotland')
city_country(country='Holland', city='Amsterdam')
city_country('London', 'England')

#8-7. Album: Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing different
#albums. Print each return value to show that the dictionaries are storing the
#album information correctly.
#Use None to add an optional parameter to make_album() that allows you to
#store the number of songs on an album. If the calling line includes a value for
#the number of songs, add that value to the album’s dictionary. Make at least
#one new function call that includes the number of songs on an album.

def make_album(artist, album, tracks=0):
    if tracks == 0:
        make_album = {'artist' : artist, 'album' : album}
    else:
        make_album = {'artist' : artist, 'album' : album, 'tracks' : tracks}
    return make_album

myAlbum = make_album('Joy Division', 'Unknown Pleasures', 10)
print(myAlbum)
myAlbum = make_album('The Cure', 'Seventeen Seconds')
print(myAlbum)
myAlbum = make_album('Echo and the Bunnymen', 'Seven Seas')
print(myAlbum)

#8-8. User Albums: Start with your program from Exercise 8-7. Write a while
#loop that allows users to enter an album’s artist and title. Once you have that
#information, call make_album() with the user’s input and print the dictionary
#that’s created. Be sure to include a quit value in the while loop.

while True:
    artist = input('Enter an artist : ')
    if artist == 'quit':
        break
    album = input('Enter an album by this artist : ')
    if album == 'quit':
        break
    myAlbum = make_album(artist, album)
    print(myAlbum)
    