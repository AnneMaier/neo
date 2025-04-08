#!/usr/bin/env python

me = {"name":"Hyun", "age" : 27, "gender": "male"}
print(me)

myname = me["name"]
print(myname)

me["age"] = 25
print(me)

dict = {}

print(dict)

me[10] = 10

print(me)

me['10'] =10
print(me)


me['job'] = 'teacher'
print(me)

me['list'] = [1,2,3]
print(me)
print(me['list'])


me[(1,2)] = 'This is value'
print(me)

me[3] = (3, 'aa', 5)
print(me)

print("=" * 40)
print(f'me[list] : {me["list"]}')
print(f'me[(1,2)] : {me[(1,2)]}')
print(f'me[3] : {me[3]}')

print("=" * 40)

print(f'me["1,2"] : {me[(1,2)]}')
me[(1,2)] = 'This is Real value'
print(f'me[(1,2)] : {me[(1,2)]}')

dict = {'a' : 1234, 'b' : 'blog' , 'c' : 3333}

# in
if 'b' in dict:
    print('b is in dict')
else:
    print('b is not in dict')

# key()

print(dict.keys())

for key in dict.keys():
    print(f'key : {key}')

# values

print(dict.values())

if 'blog' in dict.values():
    print('blog is in dict.values()')
else:
    print('blog is not in dict.values()')

for v in dict.values():
    print(f'value : {v}')

# item

print(dict.items())

for i in dict.items():
    print(f'all : {i}')
    print(f'key : {i[0]}')
    print(f'value : {i[1]}')
    print()

# get

v1  = dict.get('b')
print(f'dict.get("b") : {v1}')

v2 = dict.get('z', 'Not Exist')
print(f'dict.get("z") : {v2}')

# del
print (f'before : {dict}')

del dict['c']

print (f'after : {dict}')

# clear
dict.clear()
print(f'after clear : {dict}')