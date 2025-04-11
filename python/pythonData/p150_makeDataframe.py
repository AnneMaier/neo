import pandas as pd

sdata = {'지역': ['용산구', '마포구'], '연도': [2019, 2020]}
myframe = pd.DataFrame(data=sdata)
print(myframe)
print('-' * 50)

sdata = {'용산구': {2020: 10, 2021: 20}, '마포구': {2020: 30, 2021: 40, 2022: 50}}
myframe = pd.DataFrame(data=sdata)
print(myframe)
print('-' * 50)

sdata = {'지역': ['용산구', '마포구', '용산구', '마포구', '마포구'],
         '연도': [2019, 2020, 2021, 2020, 2021],
         '실적': [20, 30, 35, 25, 45]}
myframe = pd.DataFrame(data=sdata)
print(myframe)
print('-' * 50)