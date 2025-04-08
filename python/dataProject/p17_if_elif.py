#!/usr/bin/env python

while True:
    i = input("Input a number(q to quit) : ")

    if i == 'q' or i == 'Q':
        break

    elif i.isalpha():
        print('Please enter a valid input')
        continue
    else:
        if int(i) > 0:
            print("This is positive number")
        elif int(i) < 0:
            print("This is negative number")
        else:
            print("This is zero")