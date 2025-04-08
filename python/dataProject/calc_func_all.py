#!/usr/bin/env python

import calc_func

a = int(input("enter a number: "))
b = int(input("enter another number: "))

print(f'{a} + {b} = {calc_func.add(a, b)}')
print(f'{a} - {b} = {calc_func.sub(a, b)}')