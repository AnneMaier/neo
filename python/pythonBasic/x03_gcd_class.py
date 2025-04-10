#!/usr/bin/env python

class Gcd(object):
    def __init__(self, first_num,  second_num):
        self.first_num =  first_num
        self.second_num=  second_num

    def find_gcd(self):
        if self.first_num < self.second_num:
            self.first_num, self.second_num = self.second_num, self.first_num
        print("gcd", (self.first_num,self.second_num))
        while self.second_num != 0:
            r = self.first_num % self.second_num
            self.first_num = self.second_num
            self.second_num = r
        return self.first_num




a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

gcd = Gcd(a, b)

print(f"{a}, {b} GCD is : ", gcd.find_gcd())