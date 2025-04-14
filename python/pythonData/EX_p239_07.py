import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'mygraph.csv'

myframe = pd.read_csv(filename, index_col='type', encoding='utf-8')
myframe.index.name = '이름'
myframe.culumns.name = '시험 과목'

myframe.plot(title='학생별 누적 시험 성적시험 성적', kind='bar', rot=0, legend=True)

filename = 'p239_DataframeGraph03.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()
