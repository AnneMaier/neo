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
    return {"statusCode": 200, "message": "ok"}

@app.get('/LoanRankByDate')
async def getInfo(eventDate : Optional[str] = Query(default=datetime.now().strftime("%Y-%m-%d")), day : Optional[int] = Query(default=7) ,rank: Optional[int] = Query(default=5) , barColor : Optional[str] = Query(default='blue')):
    API_URL = "http://data4library.kr/api/loanItemSrch?"
    API_URL += "authKey=" + get_secret("doseonaru_apiKey")
    # 날짜 값 생성
    if day == None:
        day = 1
    afterEventDate = (datetime.strptime(eventDate, "%Y-%m-%d") + timedelta(days=day)).strftime("%Y-%m-%d")

    # 사건 데이터 호출 및 분석 함수화
    API_URL += "&startDt=" + eventDate
    API_URL += "&endDt=" + afterEventDate
    API_URL += "&format=json"
    API_URL += "&pageNO=1"
    API_URL += f"&pageSize={rank}"

    response = requests.get(API_URL)
    try:
        response.status_code
    except requests.exceptions.RequestException as e:
        return {"statusCode": response.status_code, "message": str(e)}
    contents = response.text
    contentsJson = json.loads(contents)
    contentsItems = contentsJson['response']['docs']
    data = contentsItems
    
    bookNameDataForGraph = []
    loanCountDataForGraph = []
    
    # API 호출 결과 만들기
    result = {"statusCode": 200, "docs": {"graphImageURL": "", "eachBookData" : []} }
    print(data)

    for eachData in data:

        # API 호출 결과에 추가
        eachDataDict = {}
        eachDataDict['ranking'] = eachData['doc']['ranking']
    # 그래프 작성을 위한 데이터 추가
        loanCountDataForGraph.append(eachData['doc']['loan_count'])

        # '권'이 여러권인 책의 경우 제목 데이터에 '권'이 추가됨
        print('vol 값:', eachData['doc'].get('vol', None))
        if eachData['doc'].get('vol', '') != '':
            eachDataDict['bookName'] = eachData['doc']['bookname'] + " " + f'<{eachData["doc"]["vol"]}권>'
            bookNameDataForGraph.append(eachData['doc']['bookname'] + " " + f'<{eachData["doc"]["vol"]}권>')
        else:
            eachDataDict['bookName'] = eachData['doc']['bookname']
            bookNameDataForGraph.append(eachData['doc']['bookname'])
        eachDataDict['author'] = eachData['doc']['authors']
        eachDataDict['isbn13'] = eachData['doc']['isbn13']
        eachDataDict['className'] = eachData['doc']['class_nm']
        eachDataDict['bookImageURL'] = eachData['doc']['bookImageURL']
        eachDataDict['loanCount'] = eachData['doc']['loan_count']
        result["docs"]["eachBookData"].append(eachDataDict)

    

    # 그래프 생성

    graphImageURL = os.path.join(GRAPHS_DIR, f"{eventDate}.png")
    plt.figure(figsize=(12, 6))
    plt.rcParams['font.family'] = 'NanumBarunGothic'
    loanCountDataForGraph = [int(x) for x in loanCountDataForGraph]
    graphDf = pd.DataFrame({
        '도서 제목': bookNameDataForGraph,
        '대출 횟수': loanCountDataForGraph
    })
    print(graphDf)
    
    plt.bar(graphDf['도서 제목'], graphDf['대출 횟수'], color=barColor)
    plt.xlabel('도서명')
    plt.ylabel('대출 횟수')
    plt.xticks(rotation=45)
    plt.ylim(0, max(graphDf['대출 횟수']) + 100)
    # 막대 위에 대출 횟수 표시
    for idx, value in enumerate(graphDf['대출 횟수']):
        plt.text(idx, value + 5, str(value), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig(graphImageURL, dpi=300, bbox_inches='tight')



    result["docs"]["graphImageURL"] = graphImageURL
    print(f"그래프 생성 완료: {graphImageURL}")




    return result
