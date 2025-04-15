import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'NanumBarunGothic'
url = 'https://www.moviechart.co.kr/rank/boxoffice'

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

mycolumn = ['순위', '제목', '개봉일', '관객수', '누적관객수']

title = '영화별 관객수와 누적관객수'

# print(soup)

infos = soup.find_all('tr')

# print(infos)

mydata0 = [i for i in range(1, 21)]

result = []
names = soup.select("td.title > a")

for i in names:
    result.append(i.text)
mydata1 = result
# print(mydata1)

release = soup.select("td.date")

result = []
for i in release:
    result.append(i.text)
mydata2 = result

result = []
audience = soup.select("td.audience")

for i in audience:
    result.append(int(i.text.strip()[:-1].replace(' ', '').replace(',', '')))
mydata3 = result

result = []
cumulative_audience = soup.select("td.cumulative")

for i in cumulative_audience:
    result.append(int(i.text.strip()[:-1].replace(' ', '').replace(',', '')))
mydata4 = result
# print(mydata4)

result = []
sales = soup.select("td.sales")

for i in sales:
    result.append(int(i.text.strip()[:-1].replace(' ', '').replace(',', '')))
mydata5 = result



myframe = pd.DataFrame(data=list(zip(mydata0, mydata1, mydata2, mydata3, mydata4)), columns=mycolumn)
myframe = myframe.set_index(keys=['순위'])
print(myframe)

filename = 'quiz_03_mvcMovie.csv'
myframe.to_csv(filename, encoding='utf8', index=False)
print(filename, ' saved...', sep='')
print('finished')

dfmovie = myframe.reindex(columns=['제목', '관객수', '누적관객수'])
print(dfmovie)

mygroup1 = dfmovie['제목']
mygroup2 = dfmovie['관객수']
mygroup3 = dfmovie['누적관객수']

df = pd.concat([mygroup2, mygroup3], axis=1)

df = df.set_index(mygroup1)

print(df)
df.columns = ['관객수', '누적관객수']
df.plot(kind='bar', title=title, rot=0)
filename = "quiz_03_mvcMovieGraph.png"
df.astype(int).plot(kind='barh', title=title, rot=0)
plt.savefig(filename, dpi=400, bbox_inches='tight', )
plt.show()