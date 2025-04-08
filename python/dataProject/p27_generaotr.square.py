#!/usr/bin/env python

mynum = [1, 2, 3, 4, 5]

def square_number(nums):
    i = 1
    while i <= len(nums):
        yield (f'Square Number: {i} * {i} = {i*i}')
        i += 1
    return

timer = square_number(mynum)
print(next(timer))
print(next(timer))
print(next(timer))
print(next(timer))
print(next(timer))
