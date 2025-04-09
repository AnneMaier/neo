#!/usr/bin/env python

numbers =  [0, 1, 2, 3]
names = ['Kim', 'Lee', 'Park', "Choi"]
print(numbers[0])
print(names[2:])
print(numbers[-1])
print(numbers+names)


# append
names.append("Hyun")
print(names)

# insert
names.insert(1, "Gang")
print(names)

# delete
del names[1]
print(names)

# remove

names.remove("Hyun")
print(names)

# pop
value  = names.pop()
print(value)


# pop
value  = names.pop(1)
print(value)


# extend

numbers.extend([(4,5,6, 4, 4, 5, 6)])
print(numbers)

# count
print(numbers.count(4))

#sort
numbers.sort()
print(numbers)

# reserve

numbers.reverse()
print(numbers)

#claear
numbers.clear()
print(numbers)