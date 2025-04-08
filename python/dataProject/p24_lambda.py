#!/usr/bin/env python

i = int(input("Enter a number: "))
j = int(input("Enter another number: "))

a = lambda i, j : i + j

print(f'Sum of {i} and {j} is {a(i, j)}')