#!/usr/bin/env python

def calc(a):

    def add(b):
        return a + b
    return add

sum = calc(1)
print(sum(2))


def hello(msg):
    messages = "Hi, "  + msg

    def say():
        print(messages)
    return say

f = hello("Hwi")

f()