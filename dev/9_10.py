#!/usr/env python3

#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod-
#ule. Make a separate file that imports Restaurant . Make a Restaurant instance,
#and call one of Restaurant ’s methods to show that the import statement is work-
#ing properly.
#This is a test to see if my ssh is working....it does
from restaurant import Restaurant

channel_club = Restaurant('the channel club', 'steak and seafood')
channel_club.describe_restaurant()
channel_club.open_restaurant()


#9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
#Store the classes User , Privileges , and Admin in one module. Create a sepa-
#rate file, make an Admin instance, and call show_privileges() to show that
#everything is working correctly.


#9-12. Multiple Modules: Store the User class in one module, and store the
#Privileges and Admin classes in a separate module. In a separate file, create
#an Admin instance and call show_privileges() to show that everything is still
#working correctly.