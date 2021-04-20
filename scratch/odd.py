#!/usr/bin/env python

userName = ['john','admin','fred','dave','susan']

for name in userName:
    if name == 'admin':
        print("Hello admin, would you like a status report?")
    else:
        print(f"Hello {name}, thanks you for logging in again.")