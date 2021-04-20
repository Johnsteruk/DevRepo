#!/usr/bin/env python

current_users = ['john','admin','fred','dave','susan','peter']
new_users = ['peter','laura','john','ann']

current_upper_users = []

for name in current_users:
    current_upper_users.append(name.upper())


for new_user in new_users:
    if new_user.upper() in current_upper_users:
        print(f"User {new_user} already exists.")
    else:
        print(f"User {new_user} is available.")