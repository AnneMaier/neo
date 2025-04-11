import pandas as pd

filename = 'SeoulLibraryInfo.csv'

df = pd.read_csv(filename, encoding='cp949')
print(df['발행년도'].tail(20))


import xml.etree.ElementTree as ET
import pandas as pd

# XML 데이터 (예시)
xml_data = """
<books>
  <book>
    <title>어린 왕자</title>
    <author>생텍쥐페리</author>
    <count>100</count>
  </book>
  <book>
    <title>해리 포터</title>
    <author>J.K. 롤링</author>
    <count>200</count>
  </book>
</books>
"""

# XML 파싱
root = ET.fromstring(xml_data)

# 데이터 추출 및 리스트에 저장
data = []
for book in root.findall('book'):
  title = book.find('title').text
  author = book.find('author').text
  count = book.find('count').text
  data.append([title, author, count])

# DataFrame 생성
df = pd.DataFrame(data, columns=['책 제목', '저자', '대출 횟수'])
    
# DataFrame 출력
print(df)