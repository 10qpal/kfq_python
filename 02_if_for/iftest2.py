# 숫자 입력받아서 홀수인지 짝수인지 판별
number = input("숫자 입력 : ")
if number.isdecimal():
    number = int(number)
    if number%2 == 0:
        print("짝수")
    else:
        print("홀수")