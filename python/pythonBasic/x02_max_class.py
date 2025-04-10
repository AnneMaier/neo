#!/usr/bin/env python

import random

class FindMax(object):
    def __init__(self, data):
        self.data = data

    def max(self):
        maxValue = self.data[0]
        for i in self.data:
            if i > maxValue:
                maxValue = i
        return maxValue


data = random.sample(range(1, 101), 10)

print(data)

data1 = FindMax(data)
print(data1.max())