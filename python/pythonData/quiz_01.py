## ex5-10.html
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mycolumns = ['이름', '국어', '영어']
filename = 'quiz_01_scoreGraph.png'

# = 여기부터
html = open('/work/neo/html/source/5/ex5-10.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
body = soup.select_one('body')
tbody = body.select_one('table').select_one('tbody')

tds = tbody.find_all('td')

print(html.read())
df = pd.DataFrame(columns=mycolumns[1:])
for i in range(0, len(tds), 3):
    df.loc[tds[i].string] = [tds[i+1].string, tds[i+2].string]
    df.index.name = mycolumns[0]
print(df)

plt.rcParams['font.family'] = 'NanumBarunGothic'
myframe = df.astype(int)

myframe.index.name = '이름'
myframe.columns.name = '국어, 영어'
myframe.plot(kind='line', rot=0, legend=True)

# plt.savefig(filename, dpi=400, bbox_inches='tight')
# print(filename + ' saved')



# print(tds)
# result = []
# for data in tds:
#     result.append(data.text)

# print(result)
