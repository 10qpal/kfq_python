import random
import time

# (1)
# cnt = 0
# qnum = int(input("몇 문제 푸실래요? "))
# input("엔터를 눌러서 문제 풀이를 시작하세요.") 
# start = time.time() 
# for i in range(0, qnum):
#     randint1 = random.randint(1,50)         # 1~50 사이 임의의 수 
#     randint2 = random.randint(1,50)
#     print("{} + {} = ".format(randint1,randint2))
#     youranswer = int(input())
#     if youranswer == randint1 + randint2:
#         print("정답")
#         cnt+=1          # cnt = cnt + 1
#     else:
#         print("오답")
# end = time.time()
# print("정답 수 / 문제 수 : {} / {}".format(cnt,i+1))
# ratio = cnt/(i+1)
# print("정답률 : %0.2f%%" % (ratio*100))
# et = end - start
# print("실제 시간 : ", et, "초")
# avgsolvetime = (i+1)*2
# print("차이 : ", abs(et-avgsolvetime), "초")

# (2)
print("---------------------")
print("----사칙연산 게임----")
print("---------------------")

operator = ["+", "-", "*", "/"]
op = random.choice(operator)
print("무작위로 선택된 사칙연산은 '%s'입니다." %op)  
#print(random.choice(operator))      # 하나 뽑아내는 함수(중복 뽑기 가능)
#print(random.sample(operator))      # 하나 뽑아내는 함수(중복 뽑기 불가능)

cnt = 0
qnum = int(input("몇 문제 푸실래요? "))  
for i in range(0, qnum):
    a = random.randint(1,50)         # 1~50 사이 임의의 수 
    b = random.randint(1,50)
    quiz = str(a) + op + str(b)
    print(quiz, '=')
    youranswer = int(input())
    if int(eval(quiz)) == youranswer:       # eval() : 문자열 명령어를 실행시켜 주는 역할
        print("정답")
        cnt+=1          # cnt = cnt + 1
    else:
        print("오답")
print("정답 수 / 문제 수 : {} / {}".format(cnt,i+1))
ratio = cnt/(i+1)
print("정답률 : %0.2f%%" % (ratio*100))