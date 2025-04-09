#!/usr/bin/env python

import sys

sys.stdout.write("Enter tne name : ")
name = sys.stdin.readline()

gender = input("Enter your gender : ")
print(f'name is {name}, gender is {gender}')