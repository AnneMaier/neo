import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from bs4 import BeautifulSoup
import time

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
myencoding = 'utf-8'
myparser = 'html.parser'
mycolumn = ['순위', '제목', '평점', '예매율', '개봉일']

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# ranking = soup.select("strong[class='rank']")
title = soup.select("strong[class='title']")
score = soup.select("span[class='percent']")
reservation_rate = soup.select("strong[class='percent'] > span")
launch_date = soup.select("span[class='txt-info'] > strong")

mydata = [i for i in range(1,20)]

result = []
for i in title:
    result.append(i.text)
mydata1 = result

result = []
for i in score:
    result.append((i.text[:2]))
mydata2 = result

result = []
for i in reservation_rate:
    result.append(i.text[:3])
mydata3 = result

result = []
for i in launch_date:
    result.append((i.text.strip()[:10]))
mydata4 = result

no = 0
info = []
for i in range(19):
    no += 1
    if mydata2[i] == '?':
        mydata2[i] = 0
    info.append((no,mydata1[i],(mydata2[i]),float(mydata3[i]),mydata4[i]))

myframe = pd.DataFrame(info, columns=mycolumn)
myframe = myframe.set_index(keys=['순위'])
print(myframe)

dfmovies = myframe.reindex(columns=['제목', '평점', '예매율'])
print(dfmovies)
df = pd.concat([dfmovies['평점'],dfmovies['예매율']],axis=1)
df = df.set_index(dfmovies['제목'])
df.columns = ['평점', '예매율']

print(df)

plt.rcParams['font.family'] = 'NanumBarunGothic'
df.astype(float).plot(kind='barh', title='영화별 평점과 예매율', rot=0)
filename = "quiz_02.cgvMovieGraph.png"
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()