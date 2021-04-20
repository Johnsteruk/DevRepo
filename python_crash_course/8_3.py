#!/usr/bin/env python3

#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
#text of a message that should be printed on the shirt. The function should print
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the
#function a second time using keyword arguments.

mySize = input("What size of T-Shirt would you like? (small/medium/large/xl/xxl) :  ")
myMessage = input("What message would you like printed on the T-Shirt? : ")

def tshirtInfo(size, message):
    print(f"You want a {size} T-Shirt that says '{message}'")

tshirtInfo(mySize,myMessage)
tshirtInfo(message=myMessage, size=mySize)

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
#by default with a message that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different
#message.
def tshirtInfo(size = 'large', message = 'I Love Python!'):
    print(f"You want a {size} T-Shirt that says '{message}'")

tshirtInfo()
tshirtInfo(size='medium')
tshirtInfo('xxl','Oracle rules!')

#8-5. Cities: Write a function called describe_city() that accepts the name of
#a city and its country. The function should print a simple sentence, such as
#Reykjavik is in Iceland . Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the
#default country.
