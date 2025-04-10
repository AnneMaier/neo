#!/usr/bin/env python

import random

data = random.sample(range(1, 101), 10)

def findMax(data):
    max = data[0]
    for i in data:
        if i > max:
            max = i
    return max

print(f'Max value is :  {findMax(data)}')