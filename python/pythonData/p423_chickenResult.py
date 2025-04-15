import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'
filename = 'xx_chicken.csv'

colnames = ['지역', '브랜드', '매장수']

myframe = pd.read_csv(filename, names=colnames, encoding='utf-8')
print(myframe)
print("-" * 50)

myframe['매장수'] = pd.to_numeric(myframe['매장수'], errors='coerce')
mygrouping = myframe.groupby(['브랜드'])['매장수']
sumSeries = mygrouping.sum()[1:]
print(sumSeries)
print("-" * 50)

mycolor = ['red', 'blue']
mytitle = '브랜드별 매장수'
myylim = [0, sumSeries.max() + 5]
myalpha = 0.7

sumSeries.plot(kind= 'bar', color=mycolor, title=mytitle, ylim=myylim, alpha=myalpha, legend=False, rot=15, grid=False)
filename = 'XX_chicken.png'

plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()
print("finished")