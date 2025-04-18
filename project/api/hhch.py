import requests, json
import pandas as pd
import os.path
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.font_manager as fm
from fastapi import FastAPI
from typing import Optional

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
async def getInfo(eventDate, rank: Optional[str] = None):
    API_URL = "http://data4library.kr/api/loanItemSrch?"
    API_URL += "authKey=" + get_secret("doseonaru_apiKey")
    # 날짜 값 생성
    before_event_date = (datetime.strptime(eventDate, "%Y-%m-%d") - timedelta(weeks=2)).strftime("%Y-%m-%d")
    after_event_date = (datetime.strptime(eventDate, "%Y-%m-%d") + timedelta(weeks=2)).strftime("%Y-%m-%d")
    items  = []
    # 사건 이전 데이터 호출 및 분석 
    API_URL += "&startDt=" + before_event_date
    API_URL += "&endDt=" + eventDate
    API_URL += "&format=json"
    API_URL += "&pageNO=1"
    API_URL += "&pageSize=5"    
    response = requests.get(API_URL)

    print('-' * 50)
    before_contents = response.text
    before_dict = json.loads(before_contents)
    before_items = before_dict['response']['docs']
    print(before_items)
    data = befoere_items
    print(data)

    return data




@app.get('/getdata')
async def getData():
    url = 'https://apis.data.go.kr/1352000/ODMS_COVID_02/callCovid02Api'

    # today = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
    today = (datetime.today() - relativedelta(months=30)).strftime("%Y%m%d")
    print(today)

    params = '?serviceKey=' + get_secret("data_apiKey")
    params += '&pageNo=1'
    params += '&numOfRows=500'
    params += '&apiType=JSON'
    params += '&status_dt=' + str(today)

    url += params
    print(url)

    response = requests.get(url)
    print(response)
    print('-' * 50)

    contents = response.text
    print(type(contents))
    print(contents)
    print('-' * 50)

    dict = json.loads(contents)
    print(type(dict))
    print(dict)
    print('-' * 50)

    items = dict['items'][0]
    print(type(items))
    print(items)
    print('-' * 50)


    item = ['gPntCnt', 'hPntCnt', 'accExamCnt', 'statusDt']

    validItem = {}
    for _ in item:
        validItem[_] = items[_]
    print(validItem)
    print('-' * 50)

    df = pd.DataFrame.from_dict(validItem, orient='index').rename(columns={0:'result'})
    print(type(df))
    print(df)
    print('-' * 50)

    return validItem
