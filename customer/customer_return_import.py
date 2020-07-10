import customerfunc      # 같은 경로일 때 파일명만으로 임포트

# custlist=[]
# page=-1
custlist=[{'name':'lee','gender':'M','email':'lee@q','birthyear':'1994'},
{'name':'kim','gender':'M','email':'kim@a','birthyear':'1996'},
{'name':'park','gender':'F','email':'park@z','birthyear':'2002'}]
page=2

def exe(choice, page):
    if choice=='I':
        page = customerfunc.insertData(page, custlist)        # 인자값 page
        # print(page)
    
    elif choice=='C':
        customerfunc.curSearch(page, custlist)
        # print(page)
    
    elif choice=='P':
        page = customerfunc.preSearch(page, custlist)
        # print(page)

    elif choice=='N':
        page = customerfunc.nextSearch(page, custlist)
        # print(page)

    elif choice=='U':
        customerfunc.updateData(custlist)
    
    elif choice=='D':
        page = customerfunc.deleteData(custlist)
        # print(page)
    
    elif choice=='Q':
        quit()
    return page 
 

              
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

    page = exe(choice, page)