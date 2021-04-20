#!/usr/env python3

#9-1. Restaurant: Make a class called Restaurant . The __init__() method for
#Restaurant should store two attributes: a restaurant_name and a cuisine_type .
#Make a method called describe_restaurant() that prints these two pieces of
#information, and a method called open_restaurant() that prints a message indi-
#cating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attri-
#butes individually, and then call both methods.
class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.name} and it serves {self.type} food.")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open.")
    
myRestaurant = Restaurant('Sam and Ellas', 'Scottish')
myRestaurant.describe_restaurant()
myRestaurant.open_restaurant()

#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
#different instances from the class, and call describe_restaurant() for each
#instance.
firstRestaurant = Restaurant('Joes', 'American')
firstRestaurant.describe_restaurant()
firstRestaurant.open_restaurant()

firstRestaurant = Restaurant('Pierres', 'French')
firstRestaurant.describe_restaurant()
firstRestaurant.open_restaurant()

firstRestaurant = Restaurant('Antonios', 'Italian')
firstRestaurant.describe_restaurant()
firstRestaurant.open_restaurant()
#9-3. Users: Make a class called User . Create two attributes called first_name
#and last_name , and then create several other attributes that are typically stored
#in a user profile. Make a method called describe_user() that prints a summary
#of the user’s information. Make another method called greet_user() that prints
#a personalized greeting to the user.
#Create several instances representing different users, and call both methods
#for each user.
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"The user is called {self.first_name.title()} {self.last_name.title()}")
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

user1 = User("John", "Campbell")
user1.describe_user()
user1.greet_user()

user2 = User("Laura", "Campbell")
user2.describe_user()
user2.greet_user()

user3 = User("Carla", "Whitaker")
user3.describe_user()
user3.greet_user()