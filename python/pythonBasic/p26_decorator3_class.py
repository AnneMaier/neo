#!/usr/bin/env python

import datetime

class DatetimeDecorator:

    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        self.func(*args, **kwargs)
        print(datetime.datetime.now())
        print()

class MainClass:
    @DatetimeDecorator
    def func1():
        print("Main function1 starts")

    def func2():
        print("Main function2 starts")

    def func3():
        print("Main function3 starts")

my = MainClass()
my.func1()