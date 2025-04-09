#!/usr/bin/env python

def division_function(a, b):
    try:
        print(a/b)
    except TypeError as e:
        print('first')
    except ZeroDivisionError as e:
        print('second')
    except Exception as e:
        print('third')


division_function("a", 1)
division_function(1, 0)
division_function(4 , 2)