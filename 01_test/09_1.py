import random,time,pickle,json,os

w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]

while True:
   print('''
   1.타자게임 
   2.문제불러오기  
   3.문제저장하기  
   4.문제 등록 수정 삭제  
   4.등수 
   5.종료하기 ''')
   menu = input("  메뉴를 선택하세요>>>")
   if menu=='1':
        n=1
        q=random.choice(w)
        input('시작!')
        start = time.time()
        while n<=5:
            print("{}번".format(n))
            print(q)
            x=input()
            if q ==x:
                print("통과!")
                n=n+1
                q=random.choice(w)
            else:
                print("오타! 다시도전!")  
        end= time.time()
        print('타자 시간 : {:.0f}초'.format(end-start))  
   elif menu=='2':
       with open('./basic/quiz/word.json','rt') as f:
            w = json.load(f)
   elif menu=='3':
       with open('./basic/quiz/word.json','wt') as f:
            json.dump(w,f,indent=4)          
   elif menu=='4':
       pass
   elif menu=='5':
       pass
   else:
       print("메뉴를 잘못 선택하셨습니다.")