import json

# 테스트용 Python Dictionary
customer = {
    'id' : 152352,
    'name' : "강진수",
    'history' : [
        {"date":"2015-03-11", "item":"iPhone"},
        {"date":"2016-02-23", "item":"Monitor"}
    ]
}

# JSON 인코딩
jsonString = json.dumps(customer)

# 문자열 출력
print(jsonString)
print(type(jsonString))

# json.dump 파일로 바로 저장
with open('test.json', 'wt') as f:
    json.dump(customer,f,indent=4)