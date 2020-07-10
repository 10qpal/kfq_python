# 일반적인 함수
def add(a,b):
    total = a+b
    print(total)
    return total

add(3,4)

def add1(a,b):
    return a+b

print(add1(4,5))

# 입력값이 없는 함수
def say():
    return 'hi'

print(say())
c = say()
print(c)

# 결괏값이 없는 함수
def add2(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))

add2(5,6)
# d = add2(5,6)
# print(d)        # 출력 : None

# 입력값, 결괏값이 없는 함수
def say2():
    print('hello')

say2()

# 여러 개의 입력값을 받는 함수
def add_many(*args):
	result = 0
	print(type(args))
	for i in args:
		result = result + i
	return result

print(add_many(1,2,3,4,5,6,7,8,9))

def add_mul(choice, *args):
	if choice == 'add':
		result = 0
		for i in args:
			result = result + i
	elif choice == 'mul':
		result = 1
		for i in args:
			result = result * i
	return result

print(add_mul('add', 1, 2, 3, 4, 5, 6))
print(add_mul('mul', 1, 2, 3, 4, 5, 6))

# 키워드 파라미터 : 딕셔너리 형태
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

# 함수의 결괏값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b
# 튜플 형태 하나로 결괏값을 돌려준다
print(add_and_mul(3,4))
# 두 개의 결괏값처럼 받고 싶다면
result1, result2 = add_and_mul(3,4)

# 초깃값
print(3,5,6,6)
# print(3,5,6,6, sep=" ", end="\n")

# 매개변수에 초깃값 미리 설정하기
# 값이 여러 개 들어가는 변수는 가장 마지막에
# 초깃값 설정한 매개변수 뒤에 초깃값 설정 안한 매개변수 X -> 초깃값 설정한 매개변수는 뒤에
def say_myself(name, old, man=True, *addr):

    print("나의 이름은 ",name,"입니다.")
    print("나이는 ",old,"살입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
    for i in addr:
        print(i)

say_myself("홍길동", 20, True, "대구", "부산", "광주")

# 함수 안에서 선언한 변수의 효력 범위
a = 1

def vartest(a):
    # global a
    a = a + 1
    print(a)
    # return a

vartest(a)
print(a)
# 1. return 이용
# 2. global 이용(좋지 않음)