myList = [5,2,1,3,4]
myList.sort()       # 리스트 : sort() 가능
print(myList)

myDict = {3:1,2:3,1:4}
#myDict.sort()       # 딕셔너리 : sort() 불가능
print(myDict)

# sorted 내장함수 이용

# str
sorted("hello")     # 출력 : 'e','h','l','l','o'

# list
sorted([5,2,1,3,4])
sorted([[2,1,3],[3,2,1],[1,2,3]])       # 출력 : [[1,2,3],[2,1,3],[3,2,1]]

# set
sorted({3,2,1})

# tuple
sorted((3,2,1))

# dict
sorted({3:1,2:3,1:4})       # 키 값을 기준으로 정렬

# 내림차순 정렬할 때 : reverse=True
sorted("hello", reverse=True)

# dict의 value 값을 기준으로 정렬하고 싶다면?
# sorted 함수의 파라미터인 key를 이용
sorted(myDict.items(), key=lambda x: x[1])      # 출력 : {3:1,2:3,1:4}

# 2번째 문자를 기준으로 정렬
sorted(['hello','name','python'], key=lambda x: x[1])       # 출력 : ['name','hello','python']