from pandas import Series


mylist = [10, 40, 30, 40]

myseries = Series(data=mylist, index=['김유신', '이순신', '강감찬', '광해군'])

print("\n Data type")
print(type(myseries))

myseries.index.name = '점수'
print('\n Index name of Series')
print(myseries.index.name)


print('\n name of index')
print(myseries.index)

print('\n value of index')
print(myseries.values)

print('\n index of series')

print('\n print information of series')
print(myseries)

print('\n repeat print')
for idx in myseries.index:
    print('index :' + idx + ', value :', str(myseries[idx]))