#!/usr/bin/env  python

n = int(input("How much number input?"))

building = list(map(int, input().split()))

print("\nbuilding:  ",building)

min_build = min(building)

print("\nminimum of building:  {}".format(min_build))


min_build_n = min(building)*n

print("\nminimum of building * n:  {}".format(min_build_n))  


sum_build = sum(building)
print("\nsum of building:  {}".format(sum_build))


result = sum_build - min_build_n

print("\nsum of building - min of building * n:  {}".format(result))