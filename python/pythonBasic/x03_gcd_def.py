#!/usr/bin/env python


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    print(f"gcd ({a} , {b})")
    return a


print(f'gcd({a} , {b}) = {gcd(a, b)}')