import requests, json
import pandas as pd
import os.path
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.font_manager as fm
from fastapi import FastAPI, Query
from typing import Optional

GRAPHS_DIR = os.path.dirname("/work/neo/project/api/graphs/")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../../secret.json')

app = FastAPI()

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

app = FastAPI()

@app.get('/')
async def HealthCheck():
    return {"status": "ok"}

@app.get('/EventLoanRankChange')
async def getInfo(eventDate : Optional[str] = Query(default=datetime.now().strftime("%Y-%m-%d")), day : Optional[int] = None ,rank: Optional[str] = None ):
    API_URL = "http://data4library.kr/api/loanItemSrch?"
    API_URL += "authKey=" + get_secret("doseonaru_apiKey")
    # 날짜 값 생성
    if day == None:
        day = 1
    afterEventDate = (datetime.strptime(eventDate, "%Y-%m-%d") + timedelta(days=day)).strftime("%Y-%m-%d")

    # 사건 데이터 호출 및 분석 함수화
    # 
    rankData = rank

    API_URL += "&startDt=" + eventDate
    API_URL += "&endDt=" + afterEventDate
    API_URL += "&format=json"
    API_URL += "&pageNO=1"
    API_URL += "&pageSize=5"    
    response = requests.get(API_URL)
    contents = response.text
    contentsJson = json.loads(contents)
    contentsItems = contentsJson['response']['docs']
    data = contentsItems
    
    bookNameDataForGraph = []
    loanCountDataForGraph = []
    
    # API 호출 결과 만들기
    result = {"docs": {"graphImageURL": "", "eachBookData" : []}}

    for eachData in data:

        # API 호출 결과에 추가
        eachDataDict = {}
        eachDataDict['ranking'] = eachData['doc']['ranking']
        eachDataDict['bookName'] = eachData['doc']['bookname']
        eachDataDict['author'] = eachData['doc']['authors']
        eachDataDict['isbn13'] = eachData['doc']['isbn13']
        eachDataDict['className'] = eachData['doc']['class_nm']
        eachDataDict['bookImageURL'] = eachData['doc']['bookImageURL']
        eachDataDict['loanCount'] = eachData['doc']['loan_count']
        result["docs"]["eachBookData"].append(eachDataDict)
    # 그래프 작성을 위한 데이터 추가
        bookNameDataForGraph.append(eachData['doc']['bookname'])
        loanCountDataForGraph.append(eachData['doc']['loan_count'])

    bookNameDataForGraph.sort()
    loanCountDataForGraph.sort()

    # 그래프 생성

    graphImageURL = os.path.join(GRAPHS_DIR, f"{eventDate}.png")
    plt.figure(figsize=(12, 6))
    plt.rcParams['font.family'] = 'NanumBarunGothic'
    plt.title = f"{eventDate} 사건일 이후 {day}일간 인기 도서 대출 횟수 비교 (상위 5위)"
    graphDf = pd.DataFrame({
        '도서 제목': bookNameDataForGraph,
        '대출 횟수': loanCountDataForGraph
    })
    
    
    plt.bar(graphDf['도서 제목'], graphDf['대출 횟수'], color='blue')
    plt.xlabel('대출 횟수')
    plt.ylabel('도서명')
    plt.savefig(graphImageURL, dpi=300, bbox_inches='tight')



    result["docs"]["graphImageURL"] = graphImageURL




    return result

#     데이터 목록
# 전/후
# 분석 그래프 이미지 주소
# 개별 책 데이터
# 도서 대출 순위
# 도서명
# 저자명
# ISBN 코드
# 권
# 도서 주제 분류
# 책 표지 이미지 URL
# 대출 권수



    # def analyzeWithGetGraph(date, API_URL, rank: Optional[str] = None, dataKind):
        
    #     dataKind = dataKindResult
    #     API_URL += "&startDt=" + date
    #     API_URL += "&endDt=" + date
    #     API_URL += "&format=json"
    #     API_URL += "&pageNO=1"
    #     API_URL += "&pageSize=5"    
    #     response = requests.get(API_URL)

    #     print('-' * 50)
    #     before_contents = response.text
    #     before_dict = json.loads(before_contents)
    #     before_items = before_dict['response']['docs']
    #     print(before_items)
    #     data = before_items
    #     print(data)

    #     return data
    
    # analyzeWithGetGraph(date=before_event_date, rank=rankData, API_URL=API_URL)
