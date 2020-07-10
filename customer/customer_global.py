import re
# custlist=[]
# page = -1
custlist=[{'name':'lee','gender':'M','email':'lee@q','birthyear':'1994'},
{'name':'kim','gender':'M','email':'kim@a','birthyear':'1996'},
{'name':'park','gender':'F','email':'park@z','birthyear':'2002'}]
page=2

def exe(choice):
    if choice=='I':
        insertData()
    
    elif choice=='C':
        curSearch()
    
    elif choice=='P':
        preSearch()

    elif choice=='N':
        nextSearch()

    elif choice=='U':
        updateData()
    
    elif choice=='D':
        deleteData()
    
    elif choice=='Q':
        quit()
            
def insertData():        
    print("고객 정보 입력")
    global page
    customer = {'name':'', 'gender':'', 'email':'','birthyear':''}
    customer['name'] = str(input("이름을 입력하세요. : "))     # str 없어도 됩니다
    
    while True:
        customer['gender'] = str(input("성별(M/m 또는 F/f)을 입력하세요. : "))
        customer['gender'] = customer['gender'].upper()
        if customer['gender'] in ('M', 'F'):
            break
    
    while True:     # 중복되지 않게 입력
        customer['email'] = str(input("이메일을 입력하세요. : "))
        check = 0       # 중복 여부 체크
        for i in custlist:
            if i['email'] == customer['email']:
                check = 1
        p = re.compile('@')     # 이메일 형식 체크
        emailcheck = p.search(customer['email'])
        if emailcheck != None and check == 0:
            break
        elif emailcheck == None:
            print("올바른 이메일 형식이 아닙니다(@이 포함되어야 합니다).")
        elif check == 1:
            print("중복되는 이메일이 있습니다.")

    while True:
        customer['birthyear'] = str(input("출생년도를 입력하세요. : "))
        if len(customer['birthyear']) == 4 and customer['birthyear'].isdecimal():
            customer['birthyear'] = int(customer['birthyear'])
            break

    custlist.append(customer)
    page+=1
    print(custlist)
    print(customer) 
    print(page)
  
def curSearch():
    print("현재 고객 정보 조회")
    global page
    if page>0:
        print("현재 페이지는 {}쪽입니다.".format(page+1))
    print(custlist[page])

def preSearch():
    print("이전 고객 정보 조회")
    global page
    if page<=0:
        print("첫번째 페이지이므로 이전 페이지 이동이 불가능합니다.")
    else:
        page-=1
        print("현재 페이지는 {}쪽입니다.".format(page+1))
    print(custlist[page])
        
def nextSearch():
    print("다음 고객 정보 조회")
    global page
    if page>=len(custlist)-1:
        print("마지막 페이지이므로 다음 페이지 이동이 불가능합니다.")
    else:
        page+=1
        print("현재 페이지는 {}쪽입니다.".format(page+1))
    print(custlist[page])

def deleteData():
    global page
    print("고객 정보 삭제")
    for i in custlist:
        print(i['name'],':',i['email'],end="   ")     # 이름과 이메일만 가져온다
    print()
    delete = input("삭제하려는 고객의 이메일을 입력하세요. : ")
    delok = 0
    for i in range(0, len(custlist)):
        if custlist[i]['email'] == delete:
            print("{} 고객님의 정보가 삭제되었습니다.".format(custlist[i]['name']))
            del custlist[i]
            delok = 1
        if delok == 1:
            break
    if delok == 0:
        print("등록되지 않은 이메일입니다.")
    for i in custlist:
        print(i['name'],':',i['email'],end="   ")     # 이름과 이메일만 가져온다
    print()
    page = len(custlist) - 1

def updateData(): 
    print("고객 정보 수정")
    for i in custlist:
        print(i['name'],':',i['email'],end="   ")     # 이름과 이메일만 가져온다
    print()
    while True:
        updateemail = input("수정하려는 고객의 이메일을 입력하세요. : ")
        idx = -1
        for i in range(0, len(custlist)):
            if custlist[i]['email'] == updateemail:      # i번째, 키 값(이메일)
                idx = i
        if idx == -1:
            print("등록되지 않은 이메일입니다.")
            break
        updatemenu = input("""
        다음 중 수정하실 정보를 입력하세요.
        name, gender, birthyear
        (수정할 정보가 없으면 exit 입력)
        """)
        if updatemenu in ('name', 'gender', 'birthyear'):
            custlist[idx][updatemenu] = input("수정할 {}을 입력하세요. : ".format(updatemenu))
            for i in custlist:
                print(i['name'],':',i['email'],end="   ")     # 이름과 이메일만 가져온다
            print()
            break
        elif updatemenu == 'exit':
            break
        else:
            print("존재하지 않는 정보입니다.")
            break


              
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()

    exe(choice)