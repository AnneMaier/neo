#!/usr/bin/env python
# Python3 샘플 코드 #


import requests
key = "	c9eb283fb128e02210af9731fb75d7771b7399f8560cecad0d924fb29470bd7a"
url = "http://data4library.kr/api/libSrch?authKey=c9eb283fb128e02210af9731fb75d7771b7399f8560cecad0d924fb29470bd7a&pageNo=1&pageSize=10".format(key)

response = requests.get(url)
print(response.request)