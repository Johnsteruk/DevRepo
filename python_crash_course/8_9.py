#!/usr/bin/env python3

#8-9. Messages: Make a list containing a series of short text messages. Pass the
#list to a function called show_messages() , which prints each text message.
#myList = ['Hello', 'Goodbye','See you later','Adios Amigo']

#def print_list(inlist):
#    for message in inlist:
#        print(message)

#print_list(myList)


#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
#Write a function called send_messages() that prints each text message and
#moves each message to a new list called sent_messages as it’s printed. After
#calling the function, print both of your lists to make sure the messages were
#moved correctly.
def print_message(myList, sent_messages):
    while myList:
        current_message = myList.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent:")
    for completed_message in sent_messages:
        print(completed_message)

myList = ['Hello', 'Goodbye','See you later','Adios Amigo']
sent_messages= []
print_message(myList, sent_messages)
show_sent_messages(sent_messages)
print(myList)
print(sent_messages)



#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
#function send_messages() with a copy of the list of messages. After calling the
#function, print both of your lists to show that the original list has retained its
#messages.
def print_message(myList, sent_messages):
    while myList:
        current_message = myList.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent:")
    for completed_message in sent_messages:
        print(completed_message)

myList = ['Hello', 'Goodbye','See you later','Adios Amigo']
sent_messages= []
print_message(myList[:], sent_messages)
show_sent_messages(sent_messages)
print(myList)
print(sent_messages)
