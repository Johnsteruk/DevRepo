#!/usr/bin/env python3

#myDict = {'john':['Glasgow', 'Amsterdam', 'Nairn']}

#prompt for user name and exit when quit
active = True
response = {}

while active:
    myName = input('Enter user name (quit to exit): ')
    listActive = True

    if myName == 'quit':
        active = False
    else:
        myPlaces = []
        while listActive:
            Destination = input('Enter desired destinations (end to quit): ')
            if Destination == 'end':
                listActive = False
            else:
                myPlaces.append(Destination)
        
        response[myName]= myPlaces

for key, values in response.items():
    print(f"The user {key} would like to go to :")
    for value in values:
        print(f"\t{value}")
