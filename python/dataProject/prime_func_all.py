#!/usr/bin/env python

import prime_func

while True:
    ipt = int(input("Enter a number(0 to quit): "))
    if ipt == 0:
        break
    if prime_func.prime(ipt):
        print("It is a prime number")
    else:
        print("It is not a prime number")