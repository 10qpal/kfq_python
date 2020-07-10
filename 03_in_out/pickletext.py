import pickle

data = {1:'python',2:'you need'}
# type dict
print(type(data))   # 파일에 저장

# 파일로 저장
with open("test.pickle",'wb') as f:
    pickle.dump(data,f)         # 자동으로 close해 줌

# 파이썬 내에서 사용 바이트 형태
# datab = pickle.dumps(data)
# print(type(datas))  # 메모리에 저장


# 파일을 읽어옴
with open("test.pickle", 'rb') as f:
    data=pickle.load(f)
    print(data)
    print(type(data))