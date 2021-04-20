#!/usr/env python3

#9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
#Add an attribute called number_served with a default value of 0. Create an
#instance called restaurant from this class. Print the number of customers the
#restaurant has served, and then change this value and print it again.
#Add a method called set_number_served() that lets you set the number
#of customers that have been served. Call this method with a new number and
#print the value again.
#Add a method called increment_number_served() that lets you increment
#the number of customers who’ve been served. Call this method with any num-
#ber you like that could represent how many customers were served in, say, a
#day of business.
class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant is called {self.name} and it serves {self.type} food.")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open.")

    def show_number_served(self):
        print(f"Number of people served = {self.number_served}")
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served
    
myRestaurant = Restaurant('Sam and Ellas', 'Scottish')
myRestaurant.show_number_served()
myRestaurant.number_served += 10
myRestaurant.show_number_served()

myRestaurant.set_number_served(45)
myRestaurant.show_number_served()
myRestaurant.increment_number_served(55)
myRestaurant.show_number_served()

#9-5. Login Attempts: Add an attribute called login_attempts to your User
#class from Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another
#method called reset_login_attempts() that resets the value of login_attempts
#to 0.
#Make an instance of the User class and call increment_login_attempts()
#several times. Print the value of login_attempts to make sure it was incremented
#properly, and then call reset_login_attempts() . Print login_attempts again to
#make sure it was reset to 0.
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user is called {self.first_name.title()} {self.last_name.title()}")
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("John", "Campbell")
print(f"{user1.login_attempts}")
user1.increment_login_attempts()
print(f"{user1.login_attempts}")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"{user1.login_attempts}")
user1.reset_login_attempts()
print(f"{user1.login_attempts}")
