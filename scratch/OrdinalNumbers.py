#!/usr/bin/env python

myNums = []

for num in range(1, 10):
    myNums.append(num)

for num in myNums:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")