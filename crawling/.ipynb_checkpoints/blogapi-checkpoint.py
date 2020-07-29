# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import json
import os
import sys
import urllib.request
client_id = "sWgdtoJD2thx3Yiuf9kj"
client_secret = "T0az9sJM2n"
encText = urllib.parse.quote("삼성전자")
url = "https://openapi.naver.com/v1/search/blog.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# for i in range(1,1000,100):
# url = "https://openapi.naver.com/v1/search/blog.json?display=100&start=%s&query=%s" %(i,encText)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
response_body = None
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

result = json.loads(response_body)
print(result['items'][0]['title'])
print(result['items'][0]['description'])
# result = json.loads(response_body)
# for i in range(0,100):
#     print(result['items'][0]['title'])
#     print(result['items'][0]['description'])
#     print()