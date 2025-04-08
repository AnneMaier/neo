#!/usr/bin/env python

def counter(max):
    t = 0

    def output():

        print("T = %d" % t)

    while t < max:
        output()
        t += 1

n = int(input("input a number: "))
counter(int(n))