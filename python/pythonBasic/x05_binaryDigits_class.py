#!/usr/bin/env python

import random

class BinaryDigits:
    def __init__(self, num, lists):
        self.num = num
        self.lists = lists

    def convert(self):
        q = self.num
        while True:
            r = q % 2
            q = q // 2
            lists.append(r)
            if q == 0:
                break
        lists.reverse()
        return lists

lists = []
num = random.randrange(4, 20)

A = BinaryDigits(num, lists)
print(f'Binary number of {num} is {A.convert()}')