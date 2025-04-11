from pandas import DataFrame

sdata = {
    '도시' : ['서울', '서울', '서울', '부산', '부산'],
    '연도' : [2020, 2021, 2022, 2021, 22022],
    '실적' : [150, 170, 360, 240, 290]
}

myindex = ['one', 'two', 'three', 'four', 'five']
myframe = DataFrame(data=sdata, index=myindex)
print('\n Type : ', type(myframe))

myframe.columns.name = 'Columns1'
print('\n Culumns Informatoin')
print(myframe.columns)

myframe.index.name = 'Index1'
print('\n Index Informatoin')
print(myframe.index)

print('\n Inner data information')
print(type(myframe.values))
print(myframe.values)

print('\n Data Type information')
print(myframe.dtypes)

print('\nContext information')
print(myframe)

print('\n row, col Trnsformation')
print(myframe.T)

print('\n Column Peroperty Useage')
mycolumns = ['연도', '도시', '실적']
newframe = DataFrame(data=sdata, index=myindex, columns=mycolumns)
print(newframe)