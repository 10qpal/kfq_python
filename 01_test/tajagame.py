import random
import time
import pickle
import json

# input("무작위로 주어지는 문장을 정확하게 치셔야 합니다.")
# input("엔터를 눌러서 문제 풀이를 시작하세요.")
# start = time.time()

# sentence=["동해물과 백두산이 마르고 닳도록", "하느님이 보우하사 우리나라 만세",
# "무궁화 삼천리 화려강산", "대한사람 대한으로 길이 보전하세"]
# rand = random.choice(sentence)
# print(rand)
# #print("글자 수 : %d" %len(rand))
# youranswer = input()
# end = time.time()
# et = end - start

# cnt = 0
# for i in range(len(rand)):
#     if rand == youranswer:
#         cnt += 1
#         if cnt > 0:
#             cnt = 1
#     else:
#         pass

# ratio = cnt / len(rand) * 100
# print("정답 수 : %d" %cnt)
# print("걸린 시간 : ", et, "초")

#소스
w = ['cat', 'dog', 'whale', 'snail', 'fox', 'frog', 'snake', 'wolf']
with open('./01_test/rank.json', 'rt') as f:     # 루트(BASIC) 아래부터 경로 작성
    rank = json.load(f)

def sortV(x):
    return x[1]

while True:
    print("1. 타자게임   2. 문제 불러오기   3. 문제 저장하기   4. 문제 등록, 수정, 삭제   5. 등수   6. 종료하기")
    menu = input("메뉴를 선택하세요 >>> ")
    if menu == '1':
        n=1
        q=random.choice(w)
        input("start")
        start=time.time()
        while n<=5:
            print("question {}".format(n))
            print(q)
            x=input()
            if q==x:
                print("OK")
                n+=1
                q=random.choice(w)
            else:
                print("NO")
        end=time.time()
        print("time : {:.0f}second".format(end-start))
        name=input("사용자 이름을 입력하세요. >>> ")
        rank[name]=float(end-start)     # 입력받은 키 값을 이용해서 밸류 저장
        print(rank)
    elif menu == '2':
        f=open("./01_test/question.pickle", 'rb')
        w=pickle.load(f)
        f.close()
        print(w)
    elif menu == '3':
        f=open("./01_test/question.pickle", 'wb')
        pickle.dump(w,f)
        f.close()
    elif menu == '4':
        print("1. 등록   2. 수정   3. 삭제")
        crudmenu=input("메뉴를 선택하세요 >>> ")
        if crudmenu=='1':
            print(w)
            quiz=input("문제 등록 >>> ")
            w.append(quiz)
            print(w)
        elif crudmenu=='2':
            print(w)
            quiz=input("수정할 문제 >>> ")
            index=w.index(quiz)
            quiz=input("수정 내용 >>> ")
            w[index]=quiz
            print(w)
        elif crudmenu=='3':
            print(w)
            quiz=input("문제 삭제 >>> ")
            w.remove(quiz)
            print(w)
        else:
            print("메뉴를 잘못 입력하셨습니다.")    
    elif menu == '5':
        #ranklist=sorted(rank.items(),key=sortV)
        ranklist=sorted(rank.items(),key=lambda x:x[1])     # 출력 : 튜플이 여러 개 있는 리스트
        num=1
        for k,v in ranklist:
            print("%d등 %s %f" %(num,k,v))       # 튜플이니까 가져올 수 있다
            num=num+1
    elif menu == '6':
        print("프로그램 종료")
        break
    else:
        print("메뉴를 잘못 입력하셨습니다.")

with open('./01_test/rank.json', 'wt') as f:
    json.dump(rank,f,indent=4)