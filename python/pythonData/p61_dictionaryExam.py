#!/usr/bin/env python

dictionary  = {'김유신': 50, '윤봉길': 40, '김구': 60}
print("Dictionary : " ,dictionary) 

for key in dictionary.keys():
   print(f'key : {key}') 

for value in dictionary.values():
   print(f'value : {value}')

for key in dictionary.keys():
   print(f'{key}의 나이는 {dictionary[key]}입니다..')

for key, value in dictionary.items():
   print(f'{key}의 나이는 {value}입니다..')

findKey = '유관순'

if findKey in dictionary.keys():
   print(f'{findKey}는  존재합니다.')
else:
   print(f'{findKey}는 존재하지 않습니다.')


result = dictionary.pop('김구')
print('After pop : ', dictionary)
print('reuslt : ', result)


dictionary.clear()
print("After clear : ", dictionary)