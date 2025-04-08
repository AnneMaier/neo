#!/usr/bin/env python


class Person(object):
    total = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

me = Person("Kibwa", 25)

print(me.name)
print(me.age)
print(me.getName())
print(me.getAge())
print(me.total)

you = Person("hwichan", 27)
print(you.getName())
print(you.getAge())
print(you.total)

